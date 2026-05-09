# Regulated Context

Patterns for operating a Data & AI platform under regulatory scrutiny. Treats regulator as a first-class consumer of the platform; classification as a first-class invariant.

## Default regulatory regimes (regulators referenced as patterns, not active filings)

| Regime | Geography | What it cares about | Pattern |
|---|---|---|---|
| OSFI-style prudential regulation | Canadian banking | Capital adequacy, risk reporting, audit trails | Audit-grade lineage end-to-end; immutable Bronze; quarantine on quality breach (not drop) |
| PIPEDA-style privacy law | Canadian privacy | Consent, retention, erasure, breach notification | UC tags + masking functions + per-purpose access |
| FinCrime-style AML/sanctions | Canadian + cross-border | Transaction monitoring, sanctions screening | Enhanced audit profile on FinCrime-relevant tables; secure tenants |
| GDPR | EU | Lawful basis, DPIA, Article 17 erasure, DPO | DPIA template + erasure runbook (`governance/`) |
| HIPAA | US healthcare | PHI handling, BAA, audit logs | PHI classification = Restricted; segregated tenants |
| SOC 2 | SaaS / B2B | Trust Service Criteria (security, availability, confidentiality) | Continuous controls + access reviews |
| SOX | US public co. financial reporting | ICFR, segregation of duties | Change management + 4-eyes approvals on financial Gold/Platinum tables |

## Three core patterns

### 1. Classification-first design

Every column carries a classification tag in Unity Catalog before it ships:

- **Public** — no restrictions; can land in any consumption layer.
- **Internal** — employees only; default for most operational data.
- **Confidential** — sensitive; masked in BI by default; cleared groups only.
- **Restricted** — regulatory PII; secure tenants only; audit-logged on every access.

PII handling is automatic at the Bronze/Silver boundary via masking functions registered in UC. See `playbooks/governance/pii-classification-medallion.md` and `playbooks/governance/masking-functions-pattern.md`.

### 2. Quarantine over drop

Failed quality records are routed to a `_quarantine` table, never silently dropped. Regulators audit BOTH what landed AND what was rejected and why.

### 3. Immutable Bronze

Bronze never updates in place. New data appends with ingest timestamp + source watermark. This is the audit-grade lineage requirement — every Silver/Gold/Platinum row can be traced to the exact Bronze record that produced it.

## DPIA-required scenarios (default triggers)

A DPIA (Data Protection Impact Assessment) is required when an initiative involves any of:

- New PII categories ingested into the platform.
- New cross-jurisdictional data movement.
- Automated decision-making with material impact (credit, employment, eligibility, pricing).
- New AI agent given access to Restricted-class data.
- Material change to retention or erasure semantics.

The `governance-audit` skill blocks initiative phase advance when `dpia_required: true` and `dpia_completed: false`. See `governance/dpia-template.md`.

## Sanitization vs. regulator references

The Sanitization Protocol (Invariant #0) bans employer / team names. Regulator names (OSFI, PIPEDA, FinCrime, GDPR, HIPAA, SOC 2, SOX) are **public** and **explicitly allowed** as generic references — they describe a regulatory pattern, not a private filing.

What's banned:
- Naming OSFI in tight conjunction with employer terms.
- Citing specific OSFI examination findings or filing IDs.
- Quoting regulators on internal-only matters.

What's allowed:
- "OSFI-style prudential regulation" as a pattern descriptor.
- General regulatory framework references in `governance/regulated-fsi-compliance-runbook.md`.

## Forks: replace this file

Forks operating under different regimes should replace this file with their own pattern table. Keep the three core patterns (classification-first, quarantine over drop, immutable Bronze) — they generalize across regulators.
