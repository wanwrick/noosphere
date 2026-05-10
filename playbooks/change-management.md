# Change Management Playbook

**Trigger:** A platform change that affects ≥1 producer's contract OR ≥1 AI consumer's view.
**Owner:** Platform Engineer (with the affected Producer PO as second-pair-of-eyes).

## Steps

1. Open a draft PR titled `change: <one-line summary>`.
2. List affected producers and AI consumers in the PR description. Pull from `data-products/data-products.yaml` `ai_consumers` lists.
3. For each affected contract: re-run `bash templates/dabs-data-product-template/scripts/validate_bundle.sh`. Must pass.
4. For each affected AI consumer: re-run `ai-consumption-contract` skill against the new view shape. Verify the 5 Principles still hold.
5. If any consumer fails the 5 Principles after the change: STOP. Either revise the change or notify the consumer owner with a deprecation window.
6. Run `bash scripts/verify_all.sh`. 9/9 must pass.
7. Notify each affected producer and consumer owner with the PR link, the contract diff, and the deprecation window (if any). 2-week minimum window for breaking changes.
8. After the deprecation window: merge the PR. Tag the release.
9. Append the change to `_Logs/evolution.md` with the version increment per `methodology/repository-conventions.md`.

## Done when

- [ ] PR merged.
- [ ] All affected producers + consumers notified.
- [ ] If breaking: deprecation window observed.
- [ ] `verify_all.sh` 9/9 passing in CI.
- [ ] `_Logs/evolution.md` stamped.

## Common failures

- **Change ships without notifying consumers.** This destroys trust faster than any technical defect. Fix the process, not the change.
- **Breaking change to a Platinum view used by an active AI agent.** The agent will silently degrade. Notify the consumer owner FIRST, ship LATER.
- **Two changes in the same week to the same contract.** Batch them. Producers cannot absorb daily contract diffs.
