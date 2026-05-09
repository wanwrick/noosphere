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

Usage:
    notion-fetch <id> > /tmp/raw.md
    python scripts/sanitize_from_notion.py \
        --source /tmp/raw.md \
        --target ip/authored/no-lac-principle.md \
        --source-id 32c7b88e-336f-8134-ae9e-e7c504061915 \
        --reviewer "Paroz Mehta" \
        --diff-out /tmp/diff.txt \
        --audit

Exit codes:
    0 — sanitized draft written; reviewer must inspect diff before commit.
    1 — banned token survived sanitization (rule needs updating). NOT written.
    2 — argument or I/O error.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Sanitization rules — mirrors scripts/lint_sanitization.sh / .gitleaks.toml.
# Each entry: (compiled regex, replacement string, category).
# ---------------------------------------------------------------------------

RULES: list[tuple[re.Pattern, str, str]] = [
    # Employer / team
    (re.compile(r"\b(Questrade|QFG|QuestBank|Quest Bank|Quest Financial Group)\b", re.I), "[Practice Name]", "employer"),
    (re.compile(r"\b(DataWizards|Data Wizards|QTG|Quest Tech Group)\b", re.I), "[Producer Team]", "team"),

    # Internal vendors / systems
    (re.compile(r"\b(Temenos|Prospector|PortfolioPlus|Intellify|CorpBI|Westway)\b", re.I), "[Internal System]", "vendor"),
    (re.compile(r"\bMartech Force\b", re.I), "[Marketing Vendor]", "vendor"),

    # JIRA / ticket codes
    (re.compile(r"\bQB-\d+\b"), "[Ticket]", "jira"),

    # Internal incident figures
    (re.compile(r"\$\d+K?\s+(incident|cost spike|disruption)", re.I), "[Incident reference]", "incident"),

    # Cross-Hub callouts
    (re.compile(r"Cross-Hub:.*$", re.M), "", "notion-marker"),

    # Stakeholder full names
    (re.compile(r"\b(Adam Muise|Mark Huang|Kriti Sood|Dan Cici|Gabriel Cortes|Yelena Hakhumyan|Hayk Danielyan|Mariano Barrionuevo|Artur Gyulambaryan)\b"), "[Stakeholder]", "stakeholder"),

    # Internal Databricks identifiers
    (re.compile(r"\bdbc-[a-f0-9]{8}-[a-f0-9]{4}\b"), "[Databricks workspace]", "databricks-id"),
    (re.compile(r"clusterId\s*[:=]\s*['\"]?\d{4}-\d{6}-[a-z0-9]{8}['\"]?"), "clusterId: [redacted]", "databricks-id"),

    # Dated meeting attributions
    (re.compile(r"\b(Jan 21, 2026|Mar 12, 2026|Mar 18, 2026|Mar 19, 2026)\b"), "[Date]", "dated-meeting"),

    # Internal team-size attributions
    (re.compile(r"\b40-45\b"), "[Team size]", "team-size"),
    (re.compile(r"\b15-20 to bank\b"), "[Org change]", "team-size"),
]

# Final lint after substitution — same rules as the bash linter would run.
FINAL_LINT: list[re.Pattern] = [
    re.compile(r"\b(Questrade|QFG|QuestBank|DataWizards|Temenos|Prospector|PortfolioPlus|Intellify|CorpBI|Westway|Martech Force|Adam Muise|Mark Huang|Kriti Sood|Dan Cici|Gabriel Cortes|Yelena Hakhumyan|Hayk Danielyan|Mariano Barrionuevo|Artur Gyulambaryan)\b", re.I),
    re.compile(r"\bQB-\d+\b"),
    re.compile(r"Cross-Hub:"),
    re.compile(r"\bdbc-[a-f0-9]{8}-[a-f0-9]{4}\b"),
]


def sanitize(text: str) -> tuple[str, dict[str, int]]:
    """Apply RULES; return sanitized text + per-category replacement count."""
    counts: dict[str, int] = {}
    for pattern, replacement, category in RULES:
        text, n = pattern.subn(replacement, text)
        if n:
            counts[category] = counts.get(category, 0) + n
    return text, counts


def final_lint(text: str) -> list[str]:
    """Return a list of any banned tokens that survived. Empty list = clean."""
    survivors: list[str] = []
    for pat in FINAL_LINT:
        for match in pat.finditer(text):
            survivors.append(match.group(0))
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
    args = parser.parse_args()

    raw = args.source.read_text() if args.source else sys.stdin.read()
    sanitized, counts = sanitize(raw)

    survivors = final_lint(sanitized)
    if survivors:
        print(f"FAIL: {len(survivors)} banned tokens survived sanitization. Update RULES in this script.", file=sys.stderr)
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
