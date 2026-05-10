# DPIA Template — Data Protection Impact Assessment

> Template DPIA. Mandatory under regulated-FSI / GDPR / PIPEDA-style regimes when triggers in `regulated-fsi-compliance-runbook.md` fire. Forks tailor to their jurisdiction.

## DPIA Header

- **DPIA ID:** `DPIA-YYYY-NNNN`
- **Initiative / Archetype:** `[ARCHETYPE-X]` or specific data product
- **Owner (DPO / privacy steward):** [Role]
- **Initiated date:** [YYYY-MM-DD]
- **Decision date:** [YYYY-MM-DD]
- **Decision:** Approved / Approved with conditions / Rejected / Re-scope required

## Section 1 — Description of processing

- What data is being processed?
- For what purpose?
- By whom (which teams, systems, agents)?
- Where does it land (which catalogs, schemas, tenants)?
- For how long is it retained?

## Section 2 — Necessity and proportionality

- Why is this processing necessary?
- What is the lawful basis (consent / contract / legitimate interest / legal obligation)?
- Are there less-invasive alternatives?
- Have data subjects been informed?
- Is the volume / scope / depth of processing proportionate to the purpose?

## Section 3 — Risks to data subjects

| Risk | Likelihood | Severity | Score |
|---|---|---|---|
| Re-identification from masked data | [low / med / high] | [low / med / high] | [1–9] |
| Cross-jurisdictional transfer exposure | … | … | … |
| Automated decision impact | … | … | … |
| Breach (confidentiality / integrity / availability) | … | … | … |
| Function creep (purpose limitation breach) | … | … | … |

## Section 4 — Mitigations

For each risk above, name the mitigation:

| Risk | Mitigation | Owner | Verification |
|---|---|---|---|
| ... | UC ABAC + masking functions | producer-platform | governance-audit skill pass |
| ... | DPIA-restricted secure-tenant residency | platform-eng | terraform plan review |
| ... | Manual override on automated decisions | product-team | UAT scenario script |

## Section 5 — Consultation

- Privacy steward consulted: [yes/no, date]
- Legal counsel consulted: [yes/no, date]
- Data subjects (or their representatives) consulted: [yes/no, summary]
- Independent review: [yes/no, name]

## Section 6 — Decision and conditions

- Decision (one of: Approved · Approved with conditions · Rejected · Re-scope required)
- Conditions (if applicable):
  - …
  - …
- Re-review trigger: [event or date]
- Sign-off (DPO or designate): [name + date]

## Section 7 — Logging

- DPIA stored at: `[path]`
- Initiative row updated in `initiatives/initiatives.yaml` with `dpia_completed: true`.
- Compliance register updated in `compliance-register.yaml`.
- Decision logged in `Knowledge/Decisions/<YYYY-MM-DD>-dpia-<archetype>.md`.

## Cross-references

- `regulated-fsi-compliance-runbook.md` — DPIA triggers.
- `data-ethics-policy.md` — ethical underpinning.
- `client-data-classification.md` — classification taxonomy referenced in Section 1.
