---
name: governance-audit
description: Run the pre-phase-advance governance audit for a regulated archetype or PII-bearing data product. Verifies DPIA, classification, masking, retention, and access obligations are met before phase advance. Use whenever an archetype with regulated=true or a data product with pii=true is about to move to the next phase, ship, or be promoted from dev to prod.
---

# governance-audit

You are running the **governance gate** that Invariant #2 from `CLAUDE.md`
demands: phase advance is blocked unless DPIA + classification + masking
obligations are demonstrably met.

## Source files (must read all five before issuing a verdict)
- `governance/compliance-register.yaml` — register of obligations.
- `governance/regulated-fsi-compliance-runbook.md` — OSFI + PIPEDA flow.
- `governance/dpia-template.md` — DPIA shape.
- `governance/client-data-classification.md` — CDMC-aligned 4-tier.
- `governance/gdpr-article-17-erasure-runbook.md` — erasure path.

## When to invoke
- An archetype in `initiatives/initiatives.yaml` is moving from
  `qualify → diagnose → design → build → embed → exit`.
- A data product with `pii: true` is being promoted dev → qa or qa → prod.
- A new producer onboarded via `data-source-10q-intake` flagged
  Tier-1/2 classification.
- Periodic audit (quarterly) on all `regulated: true` archetypes.

## Required inputs
1. Archetype ID (or data product ID) under audit.
2. Target phase (or environment) the user wants to advance to.
3. Current `dpia_completed` flag from the archetype row.

## The 7 audit checks (all must pass)
1. **DPIA exists and is current** — completed within the last 12 months,
   matches `governance/dpia-template.md` shape, signed by data ethics owner.
2. **Classification declared** — every column in the contract carries a
   tier 1–4 tag; tier-1/2 columns have a masking declaration.
3. **Masking validated** — at least one MCP-path test or unit test
   exercises every tier-1/2 column under the lowest-privilege role.
4. **Retention enforced** — retention obligation in
   `compliance-register.yaml` matches the table property in DABs.
5. **Erasure path tested** — for any column with PIPEDA / GDPR scope, the
   erasure runbook has been dry-run within the last 90 days.
6. **Access matrix matches contract** — permissions.yml ABAC tags
   reconciled against the contract's access section (no drift).
7. **Cross-jurisdictional** — if the archetype crosses borders, SCC or
   adequacy assessment attached.

## Output shape
A pass/fail audit memo:
1. **Verdict** (BLUF first sentence): PASS / CONDITIONAL PASS / FAIL.
2. Each of the 7 checks with verdict + evidence pointer.
3. If CONDITIONAL or FAIL: specific remediation list with owners + due dates.
4. Recommended next step (advance phase / block advance / re-audit on
   date X).

## Verification
- Cite the compliance register row IDs explicitly. Do not paraphrase.
- Sanitization: no employer / regulator / stakeholder names; reference
  styles like `osfi-style`, `pipeda-style` only.
- If any check is `unknown` rather than pass/fail → verdict is FAIL by
  default.

## Handoff
- On PASS: update `initiatives.yaml` `dpia_completed: true` and advance phase.
- On FAIL: log the gap to `_Logs/feedback.md` with the entry format.
- Always log the audit itself to `_Logs/sanitization-audit.md` (yes,
  governance audits live in the sanitization audit log too — same
  evidence trail).
