# Governance Runbook

**Trigger:** A `regulated: true` archetype is requesting phase advance, OR a quarterly audit is due, OR a DPIA refresh is required.
**Owner:** Governance Steward.

## Steps

1. Identify the artifact under audit: archetype ID from `initiatives/initiatives.yaml` OR data product ID from `data-products/data-products.yaml`.
2. Read the matching row. Note `dpia_required`, `dpia_completed`, `regulations`, `fee_tier_band`.
3. Read `governance/compliance-register.yaml`. Note every row applicable to this artifact.
4. Read `governance/regulated-fsi-compliance-runbook.md` for jurisdiction-specific obligations.
5. Invoke the `governance-audit` skill. It will run the 7-check audit and produce a verdict memo (PASS · CONDITIONAL · FAIL).
6. For each FAIL or CONDITIONAL check, invoke `compliance-checker` subagent against the contract (or archetype) for evidence.
7. If verdict is FAIL: do NOT advance phase. Log the gap to `_Logs/feedback.md`. Open a remediation PR with named owners and due dates.
8. If verdict is CONDITIONAL: advance phase only with sign-off from the Engagement Lead AND a stamped re-audit date.
9. If verdict is PASS: update `initiatives.yaml` (`dpia_completed: true`, `phase: <next>`) and append the audit memo to `_Logs/sanitization-audit.md`.
10. Notify the Engagement Lead and the Producer-side PO of the verdict in writing.

## Done when

- [ ] `governance-audit` skill verdict logged.
- [ ] If PASS: `initiatives.yaml` updated and committed.
- [ ] If FAIL/CONDITIONAL: remediation PR open with owners + due dates.
- [ ] Audit memo saved to `_Logs/sanitization-audit.md`.
- [ ] Engagement Lead and Producer PO notified.

## Common failures

- **DPIA "in flight" for >6 months.** That is a stalled DPIA. Treat as FAIL, escalate.
- **Tier-1/2 column with no masking declared.** Block phase advance. Apply `governance/client-data-classification.md` rubric.
- **Cross-jurisdictional data movement without SCC.** Block. Loop in legal-equivalent named role.
- **Erasure runbook untested in last 90 days.** Run a dry-run against a synthetic record before declaring PASS.
