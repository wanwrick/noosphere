# Templates — Routing

Output shapes. Each file defines the structure of one recurring deliverable.
Use them verbatim; the structure is the framework.

| File | Produces | Built on |
|---|---|---|
| `decision-memo.md` | 3-pager for VP / C-suite decisions | SCQA, Pyramid Principle |
| `status-update.md` | Progress / Plans / Problems update | 3P format |
| `rca-template.md` | Blameless post-incident review | 5 Whys, After Action Review |
| `user-story.md` | Agile story with acceptance criteria | Jira-import ready |

## Conventions

- Every template ends with a **Pre-Delivery Verification** section. Mandatory.
  It is the template's own quality gate, not a suggestion.
- Placeholders use bracket syntax (`[Your Name]`, `[Team Name]`). Never `TBD`,
  `XXX`, or angle brackets. See `methodology/repository-conventions.md`.
- Adding a template means updating the directory tree in `README.md`.

## Not to be confused with

`templates/` (lowercase) holds forkable *subprojects* — whole repos-in-a-repo.
This directory holds single-document formats. See `templates/CLAUDE.md`.

## Pairs with

`practice-context/voice-and-style.md` (BLUF, ≤25 words per sentence, banned
words), `Workflows/CLAUDE.md` (the procedure that produces the document).
