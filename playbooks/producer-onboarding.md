# Producer Onboarding Playbook

**Trigger:** A domain team has agreed to publish a data product onto the platform.
**Owner:** Producer-side Product Owner (with Platform Engineer as second-pair-of-eyes).

## Steps

1. Schedule the 10Q intake session with the producer's named owner. Block 90 minutes.
2. Run the `data-source-10q-intake` skill against the producer's request. Output: `data-contract.yml` + 2-page intake brief.
3. Save the intake brief to `data-products/<domain>-<dataset>-intake.md`.
4. Save the contract to `data-products/<domain>-<dataset>/data-contract.yml`.
5. Run `bash templates/dabs-data-product-template/scripts/validate_bundle.sh` against the contract — must pass.
6. If `regulated: true` OR `pii: true` in the contract: invoke the `governance-audit` skill BEFORE proceeding to step 7.
7. Run the `dabs-template-init` skill. Output: a deployable DABs project at `data-products/<domain>-<dataset>/`.
8. Run `python -m pytest tests/unit/ -v` inside the new project. 9/9 must pass.
9. Append the new product as a row in `data-products/data-products.yaml`.
10. Open a draft PR with the contract + bundle + brief. Title: `producer-onboarding: <domain>/<dataset>`.
11. Notify the producer's owner with the PR link and request review of the contract (not the bundle — they own the contract, the platform owns the bundle).
12. On PR merge, run the AI Consumption Contract skill (`ai-consumption-contract`) for any AI consumer flagged in the intake.

## Done when

- [ ] Contract + bundle merged to main.
- [ ] 9/9 unit tests passing in CI.
- [ ] Sanitization lint passing in CI.
- [ ] `data-products.yaml` updated.
- [ ] Producer owner has acknowledged the contract in writing (PR review approval counts).
- [ ] If regulated: `governance-audit` verdict logged to `_Logs/sanitization-audit.md`.

## Common failures

- **Producer cannot name a consumer.** Stop. There is no data product yet. Loop back to discovery.
- **Producer pushes back on classification.** Apply `governance/client-data-classification.md`. The 4-tier rubric is not negotiable.
- **Producer wants to skip the contract.** Decline. The contract is the data product. Without it, this is a one-off pipeline.
