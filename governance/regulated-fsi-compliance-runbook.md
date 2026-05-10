# Regulated FSI Compliance Runbook

> OSFI-style + PIPEDA-style compliance pattern. Generic — forks map to their actual prudential regulator and privacy regime.

## Two parallel regimes

| Regime | Pattern source | What it asks of the platform |
|---|---|---|
| **Prudential / risk** (OSFI-style) | OSFI E-23 (model risk) · OSFI B-13 (technology and cyber risk) | Audit-grade lineage · capital-adequacy reporting · model governance · operational resilience |
| **Privacy** (PIPEDA-style) | PIPEDA · GDPR · provincial privacy laws | Consent · purpose limitation · retention · access rights · breach notification |

## Five operational obligations

### 1. Audit-grade lineage end-to-end

Every fact in a regulatory report must trace to an immutable Bronze record with timestamp + source watermark. The DABs Golden Path's Bronze layer (append-only, schema-explicit, rescue-column) satisfies this by construction.

**Verification:** Pick a random Gold/Platinum row. Trace it backward through Silver to Bronze. The chain must be reproducible.

### 2. Classification + masking applied uniformly

PII columns carry classification tags + masking functions enforced at UC. Gaps are regulatory findings.

**Verification:** Run `governance-audit` skill; expect zero PII columns without `masking_function`.

### 3. Quarantine over drop

Quality breaches route to a `_quarantine` table; never silently dropped. Auditors review both what landed and what was rejected.

**Verification:** Every Silver pipeline has a `_quarantine` companion table with non-zero rows in any month with quality breaches.

### 4. Audit logging on Restricted reads

Every read of Restricted-class data is logged: who, when, query, classification of columns returned. Logs retained per regime (typically 7 years for OSFI-style, 6 years for SOX, varies for PIPEDA).

**Verification:** UC system tables show audit events; retention policy applied; spot-check a quarter's logs for anomalies.

### 5. Breach notification readiness

Pre-defined breach classification matrix + notification timeline:

| Breach severity | Notification timeline |
|---|---|
| Confirmed exfiltration of Restricted data | Per regulator timeline (typically 72h GDPR, "as soon as feasible" PIPEDA) |
| Confirmed unauthorized internal access to Restricted | Internal escalation within 24h; regulatory notification per assessment |
| Suspected breach (under investigation) | Internal incident channel; no external until confirmed |

**Verification:** Tabletop exercise quarterly. Time-to-notification measured against the matrix.

## DPIA triggers (default)

A DPIA is mandatory when initiating any of:

- New PII categories ingested.
- New cross-jurisdictional data movement.
- Automated decisions with material impact (credit, employment, eligibility, pricing, healthcare).
- New AI agent given access to Restricted-class data.
- Material change to retention or erasure semantics.
- New cross-tenant data sharing.

The `governance-audit` skill blocks initiative phase advance from `design` → `build` when `dpia_required: true` and `dpia_completed: false`.

## Onboarding new sources under regulated context

1. Run 10Q assessment (`ip/authored/10q-framework.md`).
2. Score Q7 (PII) carefully — under-classify and you'll re-do everything.
3. If `dpia_required: true`, run DPIA before pipeline design begins.
4. Apply classification taxonomy at column level.
5. Wire masking functions per column.
6. Confirm secure-tenant residency for Restricted data.
7. Wire audit logging.
8. Run `governance-audit` skill before phase advance.

## When the regulator asks

For most prudential and privacy questions, a regulator's request decomposes into:

| Question | What you produce |
|---|---|
| "What's your classification taxonomy?" | `client-data-classification.md` |
| "Show me lineage for [report row]" | UC lineage view + Bronze evidence |
| "What's your DPIA process?" | `dpia-template.md` + completed DPIAs from `compliance-register.yaml` |
| "How do you handle erasure?" | `gdpr-article-17-erasure-runbook.md` |
| "Who has accessed [Restricted column]?" | UC audit log query |
| "How do you monitor models?" | `model-risk-governance.md` + monitoring dashboards |

Pre-canned answers ≠ pre-canned compliance. The artifacts must be live, current, and demonstrable.

## Cross-references

- `client-data-classification.md` — taxonomy.
- `model-risk-governance.md` — model lifecycle.
- `dpia-template.md` — DPIA template.
- `gdpr-article-17-erasure-runbook.md` — erasure runbook.
- `compliance-register.yaml` — active obligations tracking.
- `../ip/authored/no-lac-principle.md` — Bronze immutability is a regulatory precondition, not just an architectural choice.
