# Engagement Kickoff Playbook

**Trigger:** A new engagement is starting and matches one of the codified archetypes (A–E) in `initiatives/initiatives.yaml`.
**Owner:** Engagement Lead.

## Steps

1. Identify the matching archetype. If none matches, STOP — author a new archetype dossier first using an existing one as a template.
2. Copy the archetype row in `initiatives.yaml` to a new live engagement row. Replace `ARCHETYPE-<X>` with a codename. Set `phase: qualify`.
3. Confirm the three pillar owners are named: Producer-side PO, Platform Engineer, Governance Steward (`talent/roles.md`).
4. Schedule the discovery week. Day 1: producer interviews. Day 2: platform audit. Day 3: governance baseline. Day 4: synthesis. Day 5: pitch + decision.
5. Run the `data-source-10q-intake` skill against the top-priority producer. Output: first contract candidate.
6. If `regulated: true`: run the `governance-audit` skill at Day 3 to set the governance baseline.
7. Author the engagement charter (one page, BLUF) with: scope, fee tier, phase ladder, kill criterion, named owners.
8. Pitch the charter to the decision-maker. Apply `playbooks/../ip/authored/platform-mandate-playbook.md` if the engagement requires a platform mandate.
9. On approval: advance phase from `qualify` to `diagnose`. Update `initiatives.yaml`.
10. Open the engagement repo (or branch) following `methodology/repository-conventions.md`.
11. Schedule the recurring rituals from `_Registry/Cadences.md`: standup, sprint planning, weekly synthesis, governance audit gate.

## Done when

- [ ] Engagement row in `initiatives.yaml` with named owners.
- [ ] Discovery week complete; charter authored and signed.
- [ ] First producer contract validated.
- [ ] Engagement repo or branch live.
- [ ] Recurring rituals scheduled.

## Common failures

- **Skip the archetype match.** Forces a custom playbook every engagement. Loss of leverage. Codify first.
- **Skip the kill criterion in the charter.** Without one, the engagement has no exit, only drift. Force the answer at kickoff.
- **Pillar owner doubled-up across pillars.** Acceptable only at T1 fee band. T2+ demands distinct owners.
