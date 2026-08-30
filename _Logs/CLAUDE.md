# Logs — Routing

The repo's memory. Three append-only trails; none is a working document.

| File | Trail |
|---|---|
| `evolution.md` | Version changelog: what changed, why, and the gap that triggered it |
| `feedback.md` | Corrections and preferences captured during sessions |
| `sanitization-audit.md` | Invariant #0 audit trail, lexicon-change rationale, and PII audit passes |

## Version discipline

Any structural change requires an `evolution.md` entry. Full rules in
`methodology/repository-conventions.md`. In short:

| Increment | Trigger |
|---|---|
| Major `x.0.0` | Structural overhaul. Rare. |
| Minor `1.x.0` | New file class or new routing rule. |
| Patch `1.1.x` | Edits to existing files only. |

Each entry carries: date, version, author, a changed-files table, design
decisions, and the gap that triggered the update. Bump the `## Version`
line in the root `CLAUDE.md` in the same commit.

## Feedback loop

Corrections go to `feedback.md` at session close. A gap that surfaces three or
more times is no longer a correction — it is a structural defect. Escalate it
through `Workflows/self-improvement.md` and record the fix in `evolution.md`.

## Sanitization audit

Every change to the banned-token lexicon is logged in `sanitization-audit.md`
with its rationale, as is every full PII audit pass.

**This directory is scanned by both gates. Nothing here is excluded.** An
earlier version of this file claimed `sanitization-audit.md` was exempt so it
could discuss the lexicon. That exemption was removed when the lexicon was
extracted from tracked files in v1.3.0, because excluding a file from the gate
is exactly how the lexicon sat unnoticed in the repository.

So the audit log records the **category and the reason, never the term or the
matched value**. Both logs are public. Write "employer proper noun, four
occurrences" — never the noun. Write "email address in a template" — never the
address. `scripts/lint_pii.py` will block the commit if you forget.
