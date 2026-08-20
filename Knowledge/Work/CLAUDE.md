# Work Context — Routing

Operational day-to-day context: the team, the platform, the people, the
communication norms. Distinct from `Knowledge/Frameworks/` (evergreen theory)
and `ip/` (the practice's own methodology).

| File | Contents |
|---|---|
| `team.md` | Team shape, Agile practices, stakeholder landscape |
| `platform.md` | Lakehouse reference: medallion layers, Unity Catalog, DLT, BI integration |
| `playbooks.md` | Operational frameworks snapshotted from the Work Hub |
| `communication.md` | Email, meeting, presentation, and async norms |
| `collaborators.md` | Who you work with, their domains, how to engage |

## Fork note

These files are **sample content**, carried as a worked example. A fork should
replace them wholesale with its own platform and team context. `platform.md`
and `playbooks.md` carry an explicit template note saying so.

## Sanitization

This directory is the highest-risk surface for Invariant #0: it describes real
operating context. Every name, team, vendor, and system reference must be a
bracket placeholder. Run `bash scripts/lint_sanitization.sh` after any edit.

## Live vs snapshotted

Snapshots here exist for offline portability. The live source is the Notion
Work Hub via MCP — see `_Registry/MCPs.md`. Prefer the live source when the
connector is available and the question is about current state.
