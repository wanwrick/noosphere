# GDPR Article 17 Erasure Runbook

> Operational procedure for honoring an Article 17 (right-to-erasure / right-to-be-forgotten) request. Generic — pairs with PIPEDA right-of-correction-and-deletion patterns.

## Decision tree (intake)

```
Erasure request received
        ↓
Is the requester a verified data subject?  ──── No ──→ Verify identity. If unverifiable: refuse with reason; log.
        ↓ Yes
Is at least one Article 17 condition met?
  - No longer necessary for original purpose
  - Consent withdrawn (and no other lawful basis)
  - Objection that overrides legitimate interest
  - Unlawful processing
  - Required for legal compliance
  - Collected from a child without proper consent
        ↓ Yes
Are exemptions present?
  - Freedom of expression
  - Compliance with legal obligation
  - Public interest in public health
  - Archiving / scientific research / statistics
  - Establishment / exercise / defense of legal claims
        ↓ No
EXECUTE ERASURE within 1 month (extendable to 3 months with notice).
```

## Execution steps

1. **Inventory.** Identify every system, table, view, log, backup, and downstream consumer holding the data.
2. **Cascade through Medallion layers:**
   - Bronze: erase (or pseudonymize if business need + lawful basis exists for retention).
   - Silver: erase.
   - Gold: erase or re-aggregate (if the row appears only in aggregates, aggregates may be retained).
   - Platinum: erase or re-aggregate.
3. **Cascade to derivatives.** Trained models, exported reports, partner-shared datasets — coordinate with data sharing agreements.
4. **Backups.** Document where data still exists (backups typically excluded from immediate erasure but flagged for purge on next backup cycle).
5. **Audit logs.** Audit logs themselves are typically retained (regulatory obligation). Document the carve-out in the response to the data subject.
6. **Confirmation.** Notify the data subject within the response window. Notify downstream recipients per Article 19.

## Documentation

For every erasure request:

| Field | Value |
|---|---|
| Request ID | `ERASE-YYYY-NNNN` |
| Received date | [YYYY-MM-DD] |
| Verification method | [identity-check pattern used] |
| Article 17 condition(s) cited | [list] |
| Exemptions evaluated | [list with disposition] |
| Decision | Granted / Partially granted / Refused |
| Execution date | [YYYY-MM-DD] |
| Systems affected | [list] |
| Confirmation sent | [YYYY-MM-DD] |
| Owner | [DPO or designate] |

Store under `compliance-register.yaml` linked to the request ID.

## Common challenges

- **Derived data.** A model trained on data that's now erased is itself a problem. Either re-train (cost) or document the exemption (research / statistics) carefully.
- **Cross-border copies.** Cross-jurisdictional data movement creates erasure obligations across regimes. Inventory all replicas at ingestion, not at erasure time.
- **Backups.** Industry practice is to exempt backups but purge on the next backup cycle. Document the policy.
- **Public records.** Data published under public-record obligations (e.g., regulatory filings) may be exempt. Cite the legal basis.

## Cross-references

- `regulated-fsi-compliance-runbook.md` — privacy regime patterns.
- `data-ethics-policy.md` — ethical underpinning.
- `client-data-classification.md` — Restricted-class data has the most stringent erasure obligations.
