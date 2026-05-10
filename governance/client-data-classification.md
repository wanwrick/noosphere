# Client Data Classification — CDMC-Aligned 4-Tier

> CDMC (Cloud Data Management Capabilities) framework's four-tier classification. Used in this practice as the default taxonomy in `data-contract.yml metadata.classification` and `schema.columns[].classification`.

## The four tiers

| Tier | Examples | Default access | Default masking |
|---|---|---|---|
| **Public** | Marketing materials, published research, ISO codes | Anyone | None |
| **Internal** | Internal documentation, operational metrics, business glossary | Employees | None |
| **Confidential** | Customer business data, strategic plans, financial details | Cleared groups | Masked in BI by default; raw view requires elevated access |
| **Restricted** | PII, PHI, payment data, government-sensitive | Secure tenants only | Always masked or tokenized; audit-logged on every access |

## Classification rules

1. **Default to higher tier when uncertain.** Misclassification is asymmetric: too low → regulatory finding; too high → friction. Friction is the cheaper failure.
2. **Classify at the column level**, not just the table level. A table can hold mixed-tier columns; column-level masking lets the cleared-group access stay clean.
3. **Restricted data lives only in secure tenants.** Cross-tenant movement requires explicit DPIA + steward approval.
4. **Audit logging is mandatory** for Confidential and Restricted reads.

## How this taxonomy lands in the DABs Golden Path

`data-contract.yml`:

```yaml
metadata:
  classification: confidential   # the data product's overall tier
schema:
  columns:
    - name: account_email
      classification: confidential
      pii: true
      masking_function: mask_completely
```

The bundle then:
- Tags the column in UC: `classification=confidential, pii=true, masking_function=mask_completely`.
- Applies the masking function via `ALTER COLUMN ... SET MASK`.
- Applies UC ABAC grants per tier (cleared group for Confidential; secure-tenant-only for Restricted).

## Re-classification

If a column's classification changes:

1. Update `data-contract.yml`.
2. Bump `metadata.version` (breaking change).
3. Run the `governance-audit` skill.
4. Re-deploy the bundle.
5. Notify downstream consumers via the deprecation window (`metadata.version.deprecation_window_days`).
6. Log the change in `_Logs/evolution.md`.

## Cross-references

- `data-ethics-policy.md` — ethical underpinning of classification.
- `regulated-fsi-compliance-runbook.md` — regulator-pattern application of classification.
- `../templates/dabs-data-product-template/data-contract.yml` — the runtime carrier.
- `../playbooks/governance/pii-classification-medallion.md` — how classification flows across Medallion layers.
