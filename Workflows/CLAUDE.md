# Workflows — Routing

Atomic, repeatable procedures. A workflow is the *how* for one recurring task.
Playbooks in `playbooks/` compose these; reasoning lives in `ip/`.

| File | When to run |
|---|---|
| `sanitization-pass.md` | Pulling content from Notion or any private source into the repo |
| `pii-audit-pass.md` | Before any public push, and quarterly; audits all six PII surfaces |
| `self-improvement.md` | A gap has surfaced 3+ times; run the autoresearch loop |
| `incident-response.md` | A data platform incident is open (SEV-based) |
| `executive-briefing.md` | A board deck or C-suite update is due |
| `data-storytelling.md` | An insight needs a dashboard or narrative |
| `negotiation-prep.md` | A budget, scope, or vendor negotiation is coming |

## Conventions

- Every workflow ends with a **Verification Loop** section. This is mandatory
  and machine-visible in review; a workflow without one is incomplete.
- Steps are imperative. State the trigger at the top.
- A trigger-based workflow gets a row in `_Registry/Cadences.md`.

## The three that govern the repo itself

`sanitization-pass.md` is the operational side of Invariant #0. Run it before
any commit that carries content from a private source; the pre-commit hook is
the backstop, not the process.

`pii-audit-pass.md` is the other half of Invariant #0. Sanitization protects
organizations; this protects people. They are separate obligations and they
fail differently, so they are separate gates. It is the only workflow that
looks past the working tree: four of its six surfaces — history, commit
metadata, commit subjects, and `refs/pull/*` — survive a clean `git status`,
and the last of those cannot be cleaned by a repository owner at all.

`self-improvement.md` closes the loop from `_Logs/feedback.md` to structural
change. It is the source of the three-pass verification (framework, BLUF,
action) referenced in the root Session Protocol.

## Pairs with

`_Registry/Cadences.md` (when a workflow is the scheduled response),
`Templates/CLAUDE.md` (the document a workflow produces),
`playbooks/CLAUDE.md` (multi-step engagement procedures that call these).
