# Governance — Routing

Generic, regulator-pattern-driven governance content. Forks should adapt regulator names to their actual regimes; the patterns generalize.

| File | Purpose |
|---|---|
| `data-ethics-policy.md` | Foundational ethics stance — fairness, transparency, autonomy, privacy |
| `model-risk-governance.md` | AI / ML model lifecycle governance |
| `client-data-classification.md` | CDMC-aligned 4-tier classification (Public / Internal / Confidential / Restricted) |
| `nda-template.md` | Generic mutual NDA template (forks tailor) |
| `dpia-template.md` | Data Protection Impact Assessment template |
| `regulated-fsi-compliance-runbook.md` | OSFI-style + PIPEDA-style compliance pattern |
| `gdpr-article-17-erasure-runbook.md` | GDPR right-to-erasure operational pattern |
| `compliance-register.yaml` | Tracks active compliance obligations per archetype |

## Phase-advance gate

The `governance-audit` skill runs against `initiatives/initiatives.yaml`. For any row with `regulated: true` or `pii: true`, phase advance from `design` → `build` requires:

- DPIA completed (or explicit waiver in `compliance-register.yaml`).
- Classification taxonomy applied per `client-data-classification.md`.
- Masking functions registered for PII columns.
- Audit trail wired (see `regulated-fsi-compliance-runbook.md`).

## Sanitization invariant

Every file in this folder respects the banned-token lexicon. Regulator names (OSFI, PIPEDA, GDPR, HIPAA, SOC 2, SOX) are public references and explicitly allowed; never paired with employer-banned tokens.
