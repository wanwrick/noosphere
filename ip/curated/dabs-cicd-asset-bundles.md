# CI/CD — Replace Scripts with Asset Bundles

> **Source:** Mengyu Shi. LinkedIn post — [Replace shell scripts with DABs](https://www.linkedin.com/posts/mengyu-shi-175304129_databricks-cicd-devops-share-7431430495344857088-2f58).

## Core insight

Databricks Asset Bundles (DABs) reduce CI/CD to two commands — `bundle validate` and `bundle deploy` — eliminating custom Python wrappers, fragile shell scripts, and Terraform state management.

## Before vs After

```
BEFORE (custom scripts)               AFTER (DABs)
─────────────────────────────         ─────────────────────────────
shell script                          bundle validate
  └── python wrapper                    └── catches config errors
        └── terraform                   bundle deploy
              └── state mgmt              └── deploys everything
fragile, snowflake                    reproducible, portable
team-specific                         Databricks-native
```

## Key signals

| Signal | Detail |
|---|---|
| Commands reduced to | `bundle validate` · `bundle deploy` |
| Eliminates | Custom Python wrappers · Terraform state issues |
| Portability | Works across dev / staging / prod |
| Adoption driver | Standardized config = onboarding new engineers faster |

## Why it matters

The shift is more than convenience: when deployment is two commands, engineers stop **avoiding** releases. Shipping becomes a non-event.

## When to use this in this practice

- Setting up CI/CD for any new Databricks-based data product.
- Migrating away from custom shell-script + Terraform + Python-wrapper deployment pipelines.
- The DABs Data-Contract Golden Path subproject demonstrates the pattern: `.github/workflows/ci.yml` runs `bundle validate`; `.github/workflows/deploy.yml` runs `bundle deploy`.

## Cross-references

- `dabs-custom-templates.md` (Shi) — the bootstrap pattern that pairs with deployment.
- `metadata-driven-ingestion-framework.md` (Kocyigit) — uses DABs for environment-aware deployment.
- `../authored/dabs-data-contract-golden-path.md` — this practice's runnable implementation.
