# Sanitization Audit Log

> Append-only audit trail of every sanitization pass run on Notion-sourced
> content before it lands in this repository. The Sanitization Protocol
> (see CLAUDE.md §0 and Workflows/sanitization-pass.md) is a first-class
> invariant of Noosphere v1.2.0+.

## Lexicon Change Log

Structural changes to the sanitization mechanism itself. Record the *category
and reason*, never the term — this log is public.

### 2026-08-21 — Lexicon extracted from tracked files

**What changed.** The banned-token lexicon was removed from
`.gitleaks.toml`, `scripts/lint_sanitization.sh`, and
`scripts/sanitize_from_notion.py`. All three now either load it at runtime
from a gitignored file (`.sanitization-lexicon.local`, bootstrapped from
`.sanitization-lexicon.example`) or, in the case of `.gitleaks.toml`, no
longer perform proper-noun matching at all.

**Why.** The lexicon must enumerate the employer, team, vendor, and
stakeholder proper nouns it exists to suppress. Committing it to a *public*
repository published that list in plaintext — in the very files whose purpose
was to prevent exactly that. The previous `lint_sanitization.sh` and
`.gitleaks.toml` both excluded those three files from their own scans, so the
gate structurally could not detect its own exposure.

**Consequences.**
- `.gitleaks.toml` keeps stock secret scanning plus generic structural ID
  patterns (Databricks workspace/cluster formats), which identify nobody.
- Proper-noun matching lives solely in `scripts/lint_sanitization.sh`.
- Exclusions shrank to the lexicon files alone. The sanitization tooling is
  now scanned by its own lint.
- New `--files-only` mode reports offending paths without echoing the pattern
  or matched line, so CI on this public repo cannot republish a banned token
  into its public logs.
- New `--require-real-lexicon` flag fails rather than falling back to
  placeholders.
- CI reads the lexicon from the `SANITIZATION_LEXICON` repository secret.

**Still outstanding.** Removing the terms from the working tree does not remove
them from git history. A history rewrite is tracked separately.

### 2026-08-21 — History rewritten across all branches

**What changed.** `git filter-repo --replace-text` was run over every ref,
substituting each proper noun with its placeholder across all 39 commits on all
8 branches. All branches were then force-pushed.

**Result.** A fresh clone of this repository now contains zero occurrences of
any lexicon term, in the working tree and in the full history of every branch.
`main` and `claude/extract-sanitization-lexicon` came through with their tip
trees byte-identical — current content was not touched. The six older feature
branches necessarily changed, because their tips still carried the terms.
Commit counts, authorship, and dates were preserved on every branch.
`verify_all.sh` reports 9 pass · 0 fail against the rewritten history.

**Residual exposure — NOT resolved by the rewrite.** GitHub retains
`refs/pull/<n>/head` for every pull request ever opened. Those refs are
read-only and cannot be deleted, rewritten, or force-pushed by a repository
owner. As of this entry, **29 pre-rewrite commits containing the terms remain
fetchable** via `refs/pull/1..7/head`, and the same content remains visible in
each pull request's "Files changed" and commit views on the web.

Closing that gap requires GitHub Support: ask them to garbage-collect
unreachable objects and remove the stale pull-request refs. Until they do, the
terms are still retrievable by anyone who knows where to look. A history
rewrite alone is not sufficient, and should not be recorded as if it were.

**Lesson recorded.** The first attempt at this rewrite silently corrupted 223
files. `git filter-repo --replace-text` has no comment syntax: any line lacking
`==>` is treated as a literal string to replace with `***REMOVED***`, so a lone
`#` header line replaced every `#` character in the repository. It was caught
by comparing branch tip trees against their pre-rewrite values before pushing.
Any future rewrite must diff tip trees before the push, never after.

### 2026-08-30 — Full PII audit; personal-data gate added

**Scope.** First audit covering *individuals* rather than organizations. All
six surfaces from `Workflows/pii-audit-pass.md`: working tree, history content,
commit metadata, commit messages, pull-request refs, forks. Five findings.

**Working tree was clean.** Zero emails, phone numbers, IP addresses, or
national identifiers across 240 files. `Knowledge/Work/collaborators.md` and
`team.md` were fully placeholder-ized, as their own routing file requires.

**F1 — Fork PII trap in `templates/career-command-center/` (fixed).** Ten
tracked files were designed to be populated with personal data by a session:
identity, salary expectation, work authorization, plus recruiter and
interviewer names belonging to *other people*. The only control was a comment
reading "do not commit this file to a public repository." A comment is not a
control, and the files were already tracked, so a fork inherited the trap.

Each now ships as a tracked `.example` template with the live filename
gitignored, bootstrapped by `bootstrap.sh` from the SessionStart hook — the
same example → local pattern this repo already uses for the lexicon. Generated
résumés and cover letters are ignored by extension. Verified: all ten live
files present after bootstrap, all ten ignored, none visible to `git status`.

**F2 — No PII gate existed (fixed).** The sanitization lint matched
organization proper nouns; gitleaks matched credentials and structural IDs.
Neither matched a person. A contributor pasting a real email into a document
passed every gate. Added `scripts/lint_pii.py` with 14 rules across email,
phone, SIN, SSN, payment card, IBAN, IP, postal code, street address, date of
birth, passport, and licence number. Wired into pre-commit, CI, and
`verify_all.sh` as check 10.

Two design decisions worth recording. **The rules are tracked, unlike the
lexicon** — they are generic format regexes that identify nobody, so tracking
them means a fork inherits protection with no setup. **CI runs `--files-only`**,
reporting paths but never matched text, because this repo is public and its
logs are public; the alternative republishes the data the gate exists to
suppress. Verified against a seeded file: 10 blocking categories and 1 warning
fired, every allowlisted reserved value was correctly suppressed, and
`--files-only` echoed no matched text.

**F3 — Author email in commit metadata (residual, not fixable).** 11 of 24
commits carry a personal address in author metadata. The same author used
GitHub's privacy address on the other 8, so the fix was already available and
applied inconsistently. Not retroactively fixable: rewriting metadata does not
reach `refs/pull/*`. Fixed forward — `CONTRIBUTING.md`, `SECURITY.md`, and the
career-center README now require setting `user.email` before the first commit.

**F4 — Third-party name in a commit subject (residual, needs GitHub Support).**
A commit that *removed* a private individual's attribution named that person in
its own subject line, republishing what it was removing. The pre-removal
content survives in an earlier commit, and both are reachable through
`refs/pull/*`. Same remediation path as the 2026-08-21 entry: only GitHub
Support can drop those refs. Bundle it with that request.

Distinguish this from the other names in the tree. Curated frameworks cite
published authors by name and URL, and Invariant #3 *requires* that. The test
is not "is this a name" but "did this person consent to being named here." A
cited author has. A private individual has not.

**F5 — Documented exclusion that did not exist (fixed).** `_Logs/CLAUDE.md`
stated that `sanitization-audit.md` was excluded from the lint's own scan.
That exemption was removed in the v1.3.0 lexicon extraction. The stale claim
invited a contributor to write banned tokens here believing they were exempt.
Corrected, with the reason: excluding a file from the gate is exactly how the
lexicon went unnoticed.

**Also added.** `SECURITY.md` — there was no private route to report an
exposure, so the only option was a public issue, which republishes the value to
everyone watching. `Workflows/pii-audit-pass.md` — the repeatable procedure,
including the triage table that separates a leak from a byline, an attribution,
and a false positive.

**Still outstanding.** F3 and F4 both need the GitHub Support request already
tracked in the 2026-08-21 entry. Neither is resolved by this pass and neither
should be recorded as such.

## How This Log Works

- One row per sanitization pass.
- Generated by `scripts/sanitize_from_notion.py --audit` and / or appended manually after a human review.
- Source IDs reference Notion pages; raw source content never lands in the repo.
- A v1.2.0+ release tag is blocked until every file in `ip/authored/` and `playbooks/` has at least one entry here.

## Entry Format

```
| Date | Source ID | Target file | Reviewer | Tokens replaced (by category) |
```

## Audit Trail

| Date | Source ID | Target file | Reviewer | Tokens replaced (by category) |
|------|-----------|-------------|----------|-------------------------------|
