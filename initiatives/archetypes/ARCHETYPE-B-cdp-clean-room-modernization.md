# ARCHETYPE-B — Marketing CDP + Clean Room Modernization

> **Pattern:** Customer Data Platform integration with the lakehouse + governed data clean rooms for partner / vendor data exchange. Marketing modernization without regulatory exposure.

## When this archetype fits

- Marketing function relies on third-party CDP / journey-orchestration (Braze-style platform) for outbound campaigns.
- Cross-jurisdictional partner data exchange via clean rooms (Haus / Habu / clean-room-style).
- Customer journey analytics requires both first-party and partner second-party data.

## Phases

| Phase | What happens |
|---|---|
| Qualify | DPIA scoping; data-flow inventory; partner-agreement review (consent basis, lawful basis, residency) |
| Diagnose | Data-product gap: which Platinum tables can be exposed safely? What's the consent gap? |
| Design | Clean-room contract pattern; outbound governance guardrails; Bronze→Platinum data-product spec for first marketing journey |
| Build | First Platinum data product via DABs Golden Path; clean-room exchange piloted; outbound CDP integration |
| Embed | Marketing team self-serves on Platinum; clean-room cadence operating; partner cadence operating |
| Exit | Pattern proven; second journey on the same template |

## IP applied

| IP | Role |
|---|---|
| `no-lac-principle.md` (authored) | Architecture commitment |
| `dabs-data-contract-golden-path.md` (authored) | Per-data-product implementation |
| `dashboard-factory-escape-9q.md` (curated) | Pre-build: are we building strategy or another report? |
| `data-contracts-producer-consumer.md` (curated) | Cross-org partner contracts |
| `dataplex-six-data-product-principles.md` (curated) | Cross-cloud sharing patterns |

## Regulatory pattern

PIPEDA-style + GDPR (cross-jurisdictional partner exchange). DPIA mandatory. Adequacy decision or Standard Contractual Clauses required for any cross-border movement. See `governance/dpia-template.md`.

## Operating cadence

- **Weekly:** Producer + Marketing standup (10 min); clean-room cadence with first partner.
- **Bi-weekly:** Clean-room health review (volume, quality, consent compliance).
- **Monthly:** Partner cadence (cross-org); journey performance review.
- **Quarterly:** DPIA refresh; partner agreement audit.

## Talent profile

| Role | Headcount band |
|---|---|
| Producer-side PO | 0.5 |
| Platform engineer | 1 |
| Marketing-tech integration engineer | 1 |
| Privacy steward | 0.5 |

## Common gotchas

- Treating CDP as the system of record. The lakehouse is the system of record; the CDP is an outbound engine.
- Clean-room consent assumptions. Verify consent basis with partner agreement before designing the room.
- Cross-jurisdictional data movement without DPIA. Don't.
- "Marketing data is just internal." Customer marketing data is almost always Confidential or Restricted.

## Cross-references

- `../initiatives.yaml` row id `ARCHETYPE-B-…`
- `../../governance/dpia-template.md`
- `../../ip/curated/dashboard-factory-escape-9q.md`
- `../../templates/dabs-data-product-template/`
