# Playbooks — Routing

Step-by-step playbooks. Each file is executable: a reader should be able to run the steps without re-deriving the reasoning. Reasoning lives in `ip/authored/` and `ip/curated/`.

| File | When to run |
|---|---|
| `producer-onboarding.md` | A new producer (domain team) is being attached to the platform |
| `governance-runbook.md` | A regulated phase advance, audit, or DPIA refresh |
| `change-management.md` | A platform change that affects ≥1 producer or ≥1 AI consumer |
| `engagement-kickoff.md` | A new engagement is starting (use the matching archetype) |

## Conventions

- Every playbook opens with **Trigger** (what kicks it off) and **Owner** (who runs it).
- Steps are imperative ("Run X", "Send Y"). No prose between numbered steps.
- Every step that touches data or governance points at the relevant runbook in `governance/` or skill in `.claude/skills/`.
- Every playbook ends with **Done when** — a checklist that says the playbook completed.

## Pairs with

- `_Registry/Cadences.md` — when a playbook is the cadence response.
- `Workflows/` — atomic workflows the playbooks compose.
- `governance/` — runbooks the regulated playbooks call into.
