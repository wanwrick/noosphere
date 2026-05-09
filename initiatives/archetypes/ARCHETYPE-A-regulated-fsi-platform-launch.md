# ARCHETYPE-A — Regulated FSI Platform Launch

> **Pattern:** Bronze→Platinum lakehouse build under prudential + privacy regulation. Regulatory + operational reporting served from the platform. Secure-tenant model for sensitive data.

## When this archetype fits

- New regulated entity standing up an enterprise data platform.
- Existing platform being re-architected to meet regulator expectations (audit-grade lineage, classification, masking, secure tenancy).
- Multiple consumer teams (Risk, Operations, Compliance, Finance) need self-serve access to certified data products.

## Phases (overlay on archetype-generic phases)

| Phase | What happens |
|---|---|
| Qualify | 10Q assessment for top 5–10 source systems; classification audit; regulator pattern mapping |
| Diagnose | Gap analysis: what does the regulator expect that the current state misses? |
| Design | Bronze→Platinum architecture per `no-lac-principle.md`; AI-Ready Platinum Layer per `ai-ready-platinum-layer.md`; DABs Data-Contract Golden Path adoption |
| Build | First N data products through the Golden Path; classification + masking applied; audit logging wired |
| Embed | Self-serve secure tenants live; consumer team adoption; weekly producer ritual operating |
| Exit | Platform handed to BAU; producer team owns continuous improvement; regulator pattern verified annually |

## IP applied

| IP | Role in this archetype |
|---|---|
| `no-lac-principle.md` (authored) | Architecture commitment |
| `ai-ready-platinum-layer.md` (authored) | Platinum-tier dual-interface design |
| `enterprise-claude-md.md` (authored) | Engineering team CLAUDE.md baseline |
| `dabs-data-contract-golden-path.md` (authored) | Per-data-product implementation |
| `10q-framework.md` (authored) | Source onboarding gate |
| `data-thinking-4-pillars.md` (curated) | Pre-build framework — should we build this? |
| `data-contracts-producer-consumer.md` (curated) | Producer-consumer interface formalization |
| `data-product-architecture-5-pillars.md` (curated) | Engineering pillars |
| `bain-3-layer-agentic.md` (curated) | When agentic consumption joins; Layer 3 alignment |
| `metadata-driven-ingestion-framework.md` (curated) | YAML-as-source-of-truth ingestion |

## Regulatory pattern

OSFI-style + PIPEDA-style + FinCrime-style. See `governance/regulated-fsi-compliance-runbook.md`. DPIA mandatory; classification taxonomy applied at column level; secure tenancy for Restricted-class data.

## Operating cadence

- **Weekly:** Producer-team ritual — backlog · DQ alerts · classification audit progress.
- **Bi-weekly:** Cross-functional gate review (Risk · Compliance · Producer · Consumer).
- **Monthly:** Steering committee — phase status, risk register, regulator-readiness scoring.
- **Quarterly:** Defending AI Spend 12-Q pressure test (curated/grover); regulator-pattern walkthrough.

## Talent profile

| Role | Headcount band |
|---|---|
| Producer-side PO / lead | 1 |
| Platform engineer (Terraform / DABs) | 1–2 |
| Domain engineer (per active domain) | 1 each, 4–6 total |
| Governance specialist | 1 (transitional ownership pattern — see `playbooks/change-mgmt/stakeholder-mandate-playbook.md`) |

## Common gotchas

- Under-classifying PII at intake. Under-classify once, re-do everything.
- Treating regulator readiness as Phase 6 work. It's Phase 1 work.
- Platform formalization deferred. Platform-Mandate Playbook should run *before* Phase 4 build acceleration.
- Skipping 10Q on "obvious" sources. The non-obvious gotchas live in obvious sources.

## Cross-references

- `../initiatives.yaml` row id `ARCHETYPE-A-…`
- `../../governance/regulated-fsi-compliance-runbook.md`
- `../../ip/authored/no-lac-principle.md`
- `../../templates/dabs-data-product-template/`
