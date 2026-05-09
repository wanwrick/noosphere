# Data Ethics Policy

> Foundational ethics stance for any data work this practice produces. Generic; forks should adapt to their domain.

## Core commitments

1. **Fairness.** Any model, decision, or analysis affecting individuals must be tested for disparate impact across protected attributes (race, gender, age, geography, ability) where data permits.
2. **Transparency.** Methodology, data sources, and assumptions are disclosed at the level the audience needs. *"Trust me"* is not an output.
3. **Autonomy.** Individuals have a right to opt out of automated decisions with material impact (credit, employment, eligibility, pricing, healthcare).
4. **Privacy.** Personal data is collected, used, retained, and disclosed only per the contract with the data subject and per applicable regulation.
5. **Accountability.** Every data product has a named owner. Errors are corrected; impact is acknowledged; lessons are logged in `_Logs/feedback.md`.

## Decision rules

| Question | Default answer |
|---|---|
| Should we ingest this data? | Only if there is a documented business purpose and a lawful basis (consent / contract / legitimate interest / legal obligation). |
| Should we use this data for AI training? | Only if the data subject's contract or consent covers AI use. Repurposing requires fresh consent or a DPIA. |
| Should we share this data cross-border? | Only with adequacy (GDPR-style adequacy decision, SCCs, or equivalent). DPIA required. |
| Should we use synthetic data? | Yes for testing / development. Never for external-facing claims about real-world performance. |
| Should we use a third-party model on PII? | Only with: a contract that prohibits training on the data; a DPIA; appropriate masking. |

## Disparate impact testing

For any model with material impact, before deployment:

1. Identify protected attributes in the data (or proxies).
2. Compute outcome rates per attribute.
3. Apply the four-fifths rule (or jurisdiction-specific equivalent).
4. If disparate impact present: investigate, mitigate, document, escalate.
5. Re-test post-deployment quarterly.

## When ethics conflicts with business pressure

Document the conflict. Escalate. Don't silently comply. The Decision Log (`Knowledge/Decisions/`) is the appropriate venue. *"We knew but did it anyway"* is a regulatory and reputational compounder.

## Cross-references

- `model-risk-governance.md` — operational governance for AI/ML.
- `client-data-classification.md` — classification taxonomy.
- `regulated-fsi-compliance-runbook.md` — regulatory-pattern overlay.
- `dpia-template.md` — DPIA when ethics scrutiny is highest.
