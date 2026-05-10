# ARCHETYPE-E — Legacy DW → Cloud Lakehouse Migration

> **Pattern:** Multi-quarter migration from a legacy on-prem / data-warehouse stack to a cloud lakehouse. Domain-by-domain rollout. Maintains regulatory + operational continuity throughout.

## When this archetype fits

- Existing warehouse (legacy on-prem DW class — Teradata / SQL Server / Oracle DW) is at end-of-life or no longer cost-defensible.
- Cloud lakehouse is the target; multiple consumer teams must continue operating during migration.
- Regulatory + audit obligations apply continuously through the cutover.

## Phases

| Phase | What happens |
|---|---|
| Qualify | Domain inventory; classification audit on legacy DW; consumer-team mapping; cost-projection per migration wave |
| Diagnose | Per-domain gap analysis: what's the lift to land on Bronze→Platinum patterns? |
| Design | Migration runbook per domain; rollback plan; pilot domain selected |
| Build | Pilot domain end-to-end on the new platform; consumer teams cut over; legacy domain decommissioned |
| Embed | Domain-by-domain rollout (typically 1 per month after pilot); legacy DW utilization drops |
| Exit | Last domain migrated; legacy DW formally decommissioned; cost target hit |

## IP applied

| IP | Role |
|---|---|
| `10q-framework.md` (authored) | Run on every domain at intake (legacy DW is a "source" too) |
| `no-lac-principle.md` (authored) | Architecture commitment for the destination |
| `dabs-data-contract-golden-path.md` (authored) | Per-domain implementation |
| `data-product-architecture-5-pillars.md` (curated, Czarnas) | Bounded data products replace monolithic DW |
| `cdo-top-10-deliverables.md` (curated) | Strategic framing — Deliverables 1, 6, 10 |

## Regulatory pattern

OSFI-style + SOX-equivalent. Migration window is a regulatory event. Audit-grade lineage end-to-end through the cutover. DPIA per domain; classification taxonomy reapplied (do not assume legacy classification is correct).

## Operating cadence

- **Weekly:** Migration sprint standup per domain; cutover gate reviews.
- **Bi-weekly:** Cross-domain risk + dependency review.
- **Monthly:** Steering committee — legacy DW utilization · cost-curve · risk register · regulator readiness.
- **Quarterly:** Wave retrospective + scope rebaseline.

## Talent profile

| Role | Headcount band |
|---|---|
| Producer-side migration lead | 1 |
| Platform engineer | 1 |
| Per-domain migration engineer | 1 each |
| Legacy DW SME (transitional) | 1 |

## Common gotchas

- Trying to lift-and-shift schema. The destination is a lakehouse, not a DW; modeling needs to shift.
- Ignoring downstream consumers. Cutover requires their cooperation; their consent is not free.
- "We'll fix data quality during migration." No. Data quality issues compound during migration; fix them before.
- Underestimating dual-running cost. Both stacks running during cutover doubles infrastructure cost; budget for it.
- Skipping classification audit. Legacy DW classifications are often wrong; redo at landing.

## Cross-references

- `../initiatives.yaml` row id `ARCHETYPE-E-…`
- `../../ip/authored/10q-framework.md`
- `../../ip/authored/no-lac-principle.md`
- `../../ip/curated/data-product-architecture-5-pillars.md`
