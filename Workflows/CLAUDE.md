# Workflows — Routing

Atomic, repeatable procedures. A workflow is the *how* for one recurring task.
Playbooks in `playbooks/` compose these; reasoning lives in `ip/`.

| File | When to run |
|---|---|
| `sanitization-pass.md` | Pulling content from Notion or any private source into the repo |
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

## The two that govern the repo itself

`sanitization-pass.md` is the operational side of Invariant #0. Run it before
any commit that carries content from a private source; the pre-commit hook is
the backstop, not the process.

`self-improvement.md` closes the loop from `_Logs/feedback.md` to structural
change. It is the source of the three-pass verification (framework, BLUF,
action) referenced in the root Session Protocol.

## Pairs with

`_Registry/Cadences.md` (when a workflow is the scheduled response),
`Templates/CLAUDE.md` (the document a workflow produces),
`playbooks/CLAUDE.md` (multi-step engagement procedures that call these).
