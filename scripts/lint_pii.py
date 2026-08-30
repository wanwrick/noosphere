#!/usr/bin/env python3
"""lint_pii.py — PII gate for the Noosphere Practice OS.

Scans the working tree for personal data: emails, phone numbers, national IDs,
payment cards, IP addresses, postal addresses, dates of birth, and identity
document numbers. Complements the two gates that already exist:

  scripts/lint_sanitization.sh   employer / team / vendor / stakeholder nouns
  .gitleaks.toml                 credentials and structural identifiers
  scripts/lint_pii.py            THIS FILE — personal data of any individual

Those first two never matched a person's email or phone number. A contributor
pasting real contact details into a document passed every gate in the repo.

Rules live in .pii-patterns and false positives in .pii-allowlist. Unlike the
sanitization lexicon, both are tracked: they hold generic format regexes that
identify nobody, so a fork inherits PII protection with no setup.

Usage:
    python3 scripts/lint_pii.py                  # local: shows matched text
    python3 scripts/lint_pii.py --files-only     # CI: paths only, never text
    python3 scripts/lint_pii.py --warn-as-error  # treat warn severity as block

Exit codes: 0 clean, 1 findings, 2 configuration error.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

# Paths never scanned.
#
# The two rule files are excluded because their canaries are, by design,
# strings shaped exactly like the PII they detect. Those are published test
# vectors from public documentation — they identify nobody, which is what
# makes this exclusion different in kind from the one that let the
# sanitization lexicon sit unnoticed in tracked files.
#
# Nothing else is exempt. This script is scanned by its own gate, which is how
# a card-shaped test vector spelled out in this very comment was caught: it
# passed locally only because the file was not yet staged, and failed in CI the
# moment it was. Illustrate a pattern by naming its category, never by writing
# a string that matches it.
EXCLUDED_PATHS = {
    ".pii-patterns",
    ".pii-allowlist",
    ".sanitization-lexicon.example",
    ".sanitization-lexicon.local",
}

EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", ".pytest_cache"}

BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz", ".whl",
    ".woff", ".woff2", ".ttf", ".ico", ".excalidraw",
}


@dataclass
class Rule:
    category: str
    severity: str
    regex: re.Pattern
    canary: str


@dataclass
class Finding:
    path: str
    line: int
    category: str
    severity: str
    text: str


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    files_scanned: int = 0
    rules_applied: int = 0


def repo_root() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return os.getcwd()


def load_rules(path: str) -> list[Rule]:
    """Parse .pii-patterns. Every rule must match its own canary."""
    if not os.path.exists(path):
        sys.exit(f"ERROR: pattern file not found: {path}")

    rules: list[Rule] = []
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue

            fields = line.split("\t")
            if len(fields) != 5:
                sys.exit(
                    f"ERROR: {path}:{lineno} needs 5 tab-separated fields, "
                    f"got {len(fields)}. Check that separators are real tabs."
                )

            category, flags, pattern, severity, canary = (f.strip() for f in fields)

            if severity not in ("block", "warn"):
                sys.exit(f"ERROR: {path}:{lineno} severity must be block|warn, got '{severity}'")

            re_flags = re.IGNORECASE if "i" in flags else 0
            try:
                compiled = re.compile(pattern, re_flags)
            except re.error as exc:
                sys.exit(f"ERROR: {path}:{lineno} rule [{category}] is not a valid regex: {exc}")

            # Canary check. A regex typo compiles fine and then matches nothing,
            # so the gate reports "clean" while protecting nothing — a silent
            # failure indistinguishable from success. Same guard the
            # sanitization lexicon uses.
            if not compiled.search(canary):
                sys.exit(
                    f"ERROR: {path}:{lineno} rule [{category}] does not match its own\n"
                    f"       canary {canary!r}. It would match nothing and the gate\n"
                    f"       would report a false pass. Check for doubled backslashes."
                )

            rules.append(Rule(category, severity, compiled, canary))

    if not rules:
        sys.exit(f"ERROR: {path} contained no usable rules.")
    return rules


def load_allowlist(path: str) -> list[re.Pattern]:
    """Parse .pii-allowlist. Entries are full-match regexes over matched text."""
    if not os.path.exists(path):
        return []

    patterns: list[re.Pattern] = []
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                patterns.append(re.compile(f"(?:{line})\\Z"))
            except re.error as exc:
                sys.exit(f"ERROR: {path}:{lineno} is not a valid regex: {exc}")
    return patterns


def tracked_files(root: str) -> list[str]:
    """Every file git would let you commit: tracked plus untracked-not-ignored.

    --others --exclude-standard is what makes a manual run trustworthy. Listing
    the index alone leaves a blind spot: a brand-new file is invisible until it
    is staged, so `lint_pii.py` before `git add` reports clean on exactly the
    files most likely to carry fresh personal data. --exclude-standard still
    honours .gitignore, so the career center's populated working files stay out
    of scope — they are unpublishable by construction.
    """
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        names = [n for n in out.stdout.split("\0") if n]
        if names:
            return names
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    collected: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for name in filenames:
            full = os.path.join(dirpath, name)
            collected.append(os.path.relpath(full, root))
    return collected


def scan(root: str, rules: list[Rule], allowlist: list[re.Pattern]) -> Report:
    report = Report(rules_applied=len(rules))

    for rel in tracked_files(root):
        if rel in EXCLUDED_PATHS:
            continue
        if any(part in EXCLUDED_DIRS for part in rel.split(os.sep)):
            continue
        if os.path.splitext(rel)[1].lower() in BINARY_SUFFIXES:
            continue

        full = os.path.join(root, rel)
        if not os.path.isfile(full):
            continue

        try:
            with open(full, encoding="utf-8") as fh:
                content = fh.read()
        except (UnicodeDecodeError, OSError):
            continue  # Binary or unreadable; nothing textual to match.

        report.files_scanned += 1

        for lineno, line in enumerate(content.splitlines(), 1):
            for rule in rules:
                for match in rule.regex.finditer(line):
                    text = match.group(0)
                    if any(allowed.match(text) for allowed in allowlist):
                        continue
                    report.findings.append(
                        Finding(rel, lineno, rule.category, rule.severity, text)
                    )

    return report


def emit(report: Report, files_only: bool, warn_as_error: bool) -> int:
    blocking = [f for f in report.findings if f.severity == "block"]
    warnings = [f for f in report.findings if f.severity == "warn"]

    print(f"Files scanned:  {report.files_scanned}")
    print(f"Rules applied:  {report.rules_applied}")
    print()

    def render(group: list[Finding], label: str) -> None:
        if not group:
            return
        print(f"{label} ({len(group)}):")
        by_category: dict[str, list[Finding]] = {}
        for finding in group:
            by_category.setdefault(finding.category, []).append(finding)

        for category, items in sorted(by_category.items()):
            print(f"  [{category}]")
            if files_only:
                # Paths only. This repo is public, so its CI logs are public:
                # echoing the matched text would republish the very PII the
                # gate exists to suppress. Same rule the sanitization lint
                # follows in --files-only mode.
                for path in sorted({i.path for i in items}):
                    print(f"    {path}")
            else:
                for item in items:
                    print(f"    {item.path}:{item.line}: {item.text}")
        print()

    render(blocking, "BLOCKING")
    render(warnings, "WARNING")

    if blocking or (warnings and warn_as_error):
        print("FAIL: personal data detected. Resolve before commit / merge.")
        print("      Remediation: Workflows/pii-audit-pass.md")
        print("      False positive? Add a justified entry to .pii-allowlist.")
        return 1

    if warnings:
        print("PII scan OK — 0 blocking findings (warnings above are advisory).")
    else:
        print("PII scan OK — 0 findings.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="PII gate for the Noosphere Practice OS.")
    parser.add_argument(
        "--files-only", "--ci", action="store_true", dest="files_only",
        help="Report offending paths without echoing matched text. Use anywhere output is public.",
    )
    parser.add_argument(
        "--warn-as-error", action="store_true",
        help="Treat warn-severity findings as blocking.",
    )
    parser.add_argument("--patterns", default=".pii-patterns")
    parser.add_argument("--allowlist", default=".pii-allowlist")
    args = parser.parse_args()

    root = repo_root()
    os.chdir(root)

    print(f"PII lint over: {root}")
    print(f"Patterns:      {args.patterns}")
    print(f"Allowlist:     {args.allowlist}")
    print()

    rules = load_rules(args.patterns)
    allowlist = load_allowlist(args.allowlist)
    report = scan(root, rules, allowlist)
    return emit(report, args.files_only, args.warn_as_error)


if __name__ == "__main__":
    sys.exit(main())
