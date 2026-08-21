# Logs — Routing

The repo's memory. Three append-only trails; none is a working document.

| File | Trail |
|---|---|
| `evolution.md` | Version changelog: what changed, why, and the gap that triggered it |
| `feedback.md` | Corrections and preferences captured during sessions |
| `sanitization-audit.md` | Invariant #0 audit trail and the rationale behind lexicon changes |

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

Every change to the banned-token lexicon in `scripts/lint_sanitization.sh` is
logged here with its rationale. This file is excluded from the lint's own scan
so it can discuss the lexicon; that exclusion is deliberate and must not be
copied to other files.
