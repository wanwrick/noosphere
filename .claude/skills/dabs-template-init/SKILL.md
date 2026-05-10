---
name: dabs-template-init
description: Bootstrap a new Databricks Asset Bundle data product from the DABs Data-Contract Golden Path template. Turns one data-contract.yml into Bronze ingestion + Silver DLT expectations + UC ABAC + Platinum AI-ready views + CI/CD gates. Use when a new data product has been intake'd via 10Q and is ready for build.
---

# dabs-template-init

You are bootstrapping a fresh DABs project from
`templates/dabs-data-product-template/`. This is the **forkable Golden
Path** — one contract, four medallion layers, full CI/CD.

## Source IP
- Authored: `ip/authored/dabs-data-contract-golden-path.md`.
- Authored: `ip/authored/ai-ready-platinum-layer.md` (Platinum publish).
- Curated: `ip/curated/dabs-cicd-asset-bundles.md`.
- Curated: `ip/curated/dabs-custom-templates.md`.

## When to invoke
- After `data-source-10q-intake` produces a complete `data-contract.yml`.
- "Spin up a new data product", "init DABs project", "fork the Golden Path".

## Required inputs
1. Path to a valid `data-contract.yml` (validates against
   `data-contract.schema.json`).
2. Target catalog + schema in Unity Catalog (placeholders OK if regulated
   review pending).
3. Environment(s): dev / qa / prod.

## Steps
1. Copy `templates/dabs-data-product-template/` to the new product
   location (e.g. `data-products/<domain>-<dataset>/`).
2. Move the user's `data-contract.yml` to the project root and validate:
   `bash scripts/validate_bundle.sh` (6 checks must pass).
3. Render `databricks.yml` — fill catalog, schema, env, host placeholders.
4. Render `resources/permissions.yml` from the contract's access matrix
   and classification (UC ABAC tags driven by Tier 1–4).
5. Render `resources/pipeline.yml` for Silver DLT expectations from the
   contract's `quality` block.
6. Run `python -m pytest tests/unit/ -v` (must be 9/9 green).
7. Render `.github/workflows/ci.yml` so PRs run validate + unit tests.
8. Generate the initial AI Consumption Contract:
   `python scripts/generate_ai_contract.py` (reads the contract,
   produces the Platinum-layer publish manifest).

## Output shape
- A working DABs project at `data-products/<domain>-<dataset>/`.
- All template placeholders replaced; no `<TODO>` left.
- `validate_bundle.sh` exits 0; pytest exits 0.
- A README.md at the project root explaining the contract and the
  deploy commands.

## Verification
- Sanitization: no employer / team / vendor / workspace ID anywhere.
- Contract still validates after rendering (re-run schema check).
- Permissions match the classification declared in the contract.
- If `pii: true` or `regulated: true` → invoke `governance-audit` before
  declaring init complete.

## Handoff
- If governance gate triggered: run `governance-audit` skill.
- If AI consumption: run `ai-consumption-contract` skill on the
  Platinum view.
- Update `data-products/data-products.yaml` with the new product row.
- Phase advance in `initiatives/initiatives.yaml` if the product is part
  of an active archetype.
