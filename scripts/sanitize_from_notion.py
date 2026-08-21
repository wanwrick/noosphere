#!/usr/bin/env python3
"""sanitize_from_notion.py — human-driven helper for refreshing IP from Notion.

Pipeline:
    1. Read raw markdown sourced from `notion-fetch` (passed via stdin or a
       `--source` file).
    2. Apply the banned-token lexicon to produce a sanitized draft.
    3. Emit the sanitized draft to `--target` (or stdout) plus a unified diff
       to `--diff-out` (or stderr) so a human can review what changed.
    4. Append an entry to `_Logs/sanitization-audit.md` if `--audit` is passed.

The script does NOT auto-commit. Human review of the diff is mandatory before
the sanitized draft can land in the repo. This is what keeps the sanitization
invariant defensible — every transform is logged with a reviewer name.

THE LEXICON IS NOT STORED IN THIS REPOSITORY.
    The banned-token lexicon enumerates the employer / team / vendor /
    stakeholder proper nouns it exists to protect. Committing it to a public
    repo publishes exactly what it is meant to hide. It loads at runtime from
    a gitignored file; see .sanitization-lexicon.example for the format.

Usage:
    cp .sanitization-lexicon.example .sanitization-lexicon.local   # once
    notion-fetch <id> > /tmp/raw.md
    python scripts/sanitize_from_notion.py \
        --source /tmp/raw.md \
        --target ip/authored/no-lac-principle.md \
        --source-id <notion-page-id> \
        --reviewer "<your name>" \
        --diff-out /tmp/diff.txt \
        --audit

Exit codes:
    0 — sanitized draft written; reviewer must inspect diff before commit.
    1 — banned token survived sanitization (rule needs updating). NOT written.
    2 — argument, I/O, or lexicon error.
    3 — only placeholder terms available and --require-real-lexicon was passed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import os
import re
import sys
from pathlib import Path

EXAMPLE_LEXICON = ".sanitization-lexicon.example"
LOCAL_LEXICON = ".sanitization-lexicon.local"

Rule = tuple[re.Pattern, str, str]


def resolve_lexicon(repo_root: Path, explicit: Path | None) -> tuple[Path, bool]:
    """Return (lexicon_path, using_placeholders). First match wins."""
    if explicit:
        if not explicit.is_file():
            raise FileNotFoundError(f"--lexicon points at a missing file: {explicit}")
        return explicit, False

    env = os.environ.get("NOOSPHERE_LEXICON")
    if env:
        path = Path(env)
        if not path.is_file():
            raise FileNotFoundError(f"NOOSPHERE_LEXICON points at a missing file: {path}")
        return path, False

    local = repo_root / LOCAL_LEXICON
    if local.is_file():
        return local, False

    example = repo_root / EXAMPLE_LEXICON
    if example.is_file():
        return example, True

    raise FileNotFoundError(
        f"No lexicon found. Expected one of: --lexicon, $NOOSPHERE_LEXICON, "
        f"{LOCAL_LEXICON}, {EXAMPLE_LEXICON}"
    )


def load_lexicon(path: Path) -> list[Rule]:
    """Parse a TAB-separated lexicon into compiled rules.

    Format per line: category<TAB>flags<TAB>pattern<TAB>replacement[<TAB>canary]
    Flags: 'i' case-insensitive, 'm' multiline, '-' none. Combine as 'im'.

    A rule may carry a canary: a sample string the pattern must match. This is
    load-bearing. A regex typo (a doubled backslash, an unbalanced group)
    compiles fine and then matches nothing, so the gate reports "clean" while
    protecting nothing — silent failure indistinguishable from success. A
    canary that does not match is a hard error.
    """
    rules: list[Rule] = []
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        # rstrip('\n') only — a trailing tab means "replace with empty string".
        line = raw_line.rstrip("\r")
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        fields = line.split("\t")
        if len(fields) < 4:
            print(
                f"WARN: {path}:{lineno} skipped — need 4 tab-separated fields, got {len(fields)}",
                file=sys.stderr,
            )
            continue

        category, flags, pattern, replacement = fields[0], fields[1], fields[2], fields[3]
        canary = fields[4] if len(fields) > 4 else ""

        compiled_flags = 0
        if "i" in flags:
            compiled_flags |= re.I
        if "m" in flags:
            compiled_flags |= re.M

        try:
            compiled = re.compile(pattern, compiled_flags)
        except re.error as exc:
            raise ValueError(f"{path}:{lineno} invalid regex {pattern!r}: {exc}") from exc

        if canary and not compiled.search(canary):
            raise ValueError(
                f"{path}:{lineno} rule [{category}] does not match its own canary.\n"
                f"    pattern: {pattern!r}\n"
                f"    canary:  {canary!r}\n"
                f"    This rule would match nothing and the gate would report a "
                f"false pass. Check for doubled backslashes."
            )

        rules.append((compiled, replacement, category))

    return rules


def sanitize(text: str, rules: list[Rule]) -> tuple[str, dict[str, int]]:
    """Apply rules; return sanitized text + per-category replacement count."""
    counts: dict[str, int] = {}
    for pattern, replacement, category in rules:
        text, n = pattern.subn(replacement, text)
        if n:
            counts[category] = counts.get(category, 0) + n
    return text, counts


def final_lint(text: str, rules: list[Rule]) -> list[str]:
    """Return any banned tokens that survived substitution. Empty list = clean.

    Rules whose replacement is empty are skipped: deleting a marker cannot be
    verified by re-matching the same pattern against the result.
    """
    survivors: list[str] = []
    for pattern, replacement, _category in rules:
        if replacement == "":
            continue
        survivors.extend(match.group(0) for match in pattern.finditer(text))
    return survivors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, help="Raw Notion markdown file. Defaults to stdin.")
    parser.add_argument("--target", type=Path, help="Where to write sanitized draft. Defaults to stdout.")
    parser.add_argument("--source-id", required=True, help="Notion page ID for the audit trail.")
    parser.add_argument("--reviewer", required=True, help="Human reviewer name for the audit trail.")
    parser.add_argument("--diff-out", type=Path, help="Where to write a unified diff for review. Defaults to stderr.")
    parser.add_argument("--audit", action="store_true", help="Append an entry to _Logs/sanitization-audit.md.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repo root (for the audit log).")
    parser.add_argument("--lexicon", type=Path, help="Explicit lexicon path. Overrides $NOOSPHERE_LEXICON.")
    parser.add_argument(
        "--require-real-lexicon",
        action="store_true",
        help="Exit 3 rather than running with placeholder terms.",
    )
    args = parser.parse_args()

    try:
        lexicon_path, using_placeholders = resolve_lexicon(args.repo_root, args.lexicon)
        rules = load_lexicon(lexicon_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not rules:
        print(f"ERROR: lexicon {lexicon_path} contained no usable rules.", file=sys.stderr)
        return 2

    print(f"Lexicon: {lexicon_path} ({len(rules)} rules)", file=sys.stderr)

    if using_placeholders:
        print(
            "WARNING: running with PLACEHOLDER terms — YOU ARE NOT PROTECTED.\n"
            f"         cp {EXAMPLE_LEXICON} {LOCAL_LEXICON} and replace the\n"
            "         placeholders with your real terms.",
            file=sys.stderr,
        )
        if args.require_real_lexicon:
            print("FAIL: --require-real-lexicon was passed but only placeholders are available.", file=sys.stderr)
            return 3

    raw = args.source.read_text() if args.source else sys.stdin.read()
    sanitized, counts = sanitize(raw, rules)

    survivors = final_lint(sanitized, rules)
    if survivors:
        print(f"FAIL: {len(survivors)} banned tokens survived sanitization. Update the lexicon.", file=sys.stderr)
        for s in survivors[:10]:
            print(f"  - {s!r}", file=sys.stderr)
        return 1

    diff = difflib.unified_diff(
        raw.splitlines(keepends=True),
        sanitized.splitlines(keepends=True),
        fromfile="raw",
        tofile="sanitized",
    )
    diff_text = "".join(diff)

    if args.target:
        args.target.parent.mkdir(parents=True, exist_ok=True)
        args.target.write_text(sanitized)
    else:
        sys.stdout.write(sanitized)

    if args.diff_out:
        args.diff_out.write_text(diff_text)
    else:
        sys.stderr.write(diff_text)

    if args.audit:
        audit_path = args.repo_root / "_Logs" / "sanitization-audit.md"
        ts = dt.date.today().isoformat()
        target_label = str(args.target) if args.target else "<stdout>"
        total = sum(counts.values())
        cat_summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "none"
        entry = (
            f"\n| {ts} | `{args.source_id}` | `{target_label}` | "
            f"{args.reviewer} | {total} ({cat_summary}) |"
        )
        with audit_path.open("a") as fh:
            fh.write(entry)
        print(f"Audit appended: {audit_path}", file=sys.stderr)

    print("Sanitization OK. Review the diff before committing.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
