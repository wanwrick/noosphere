# Role Archetypes

Seven roles the practice runs against. A small engagement collapses several into one person. A large engagement keeps them distinct.

| Role | Pillar | Owns | Hands off to |
|------|--------|------|--------------|
| Producer-side Product Owner | Producer | The contract, the intake, the SLA | Platform engineer (bundle), Governance steward (audit) |
| Platform Engineer | Platform | The bundle, the rendering, the CI gate | Producer PO (changes), AI Consumer (Platinum view) |
| Governance Steward | Governance | Classification, masking, DPIA, audit trail | Decision-maker (gate verdict), Producer PO (remediation) |
| AI Consumer Owner | Producer of AI | The agent, the use case, the consumption contract | Platform engineer (Platinum view), Governance steward (DPIA) |
| Data Domain Lead | Producer (domain) | The business definition, the glossary, the metric ownership | Producer PO (contract), AI Consumer Owner (semantics) |
| Engagement Lead | Practice | Phase advance, fee tier, archetype scorecard | All above |
| Practice Author | Practice | The IP, the playbooks, the standards (this repo) | Engagement Lead (application), All roles (uplift) |

## Role principles

- **Every contract has exactly one Producer PO.** Joint ownership is no ownership.
- **Every audit has exactly one Governance Steward.** Distributed responsibility for compliance is a known anti-pattern.
- **The Practice Author writes IP, not contracts.** If the author is in the contract loop, the practice is not yet leveraged.
- **Engagement Lead reads the scorecard weekly.** The four colors (cognitive clarity · data fluency · decision velocity · organizational adoption) decide phase advance more than vibes.
