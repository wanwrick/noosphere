# DABs Custom Templates — Stop Starting From a Blank Page

> **Source:** Mengyu Shi. LinkedIn post — [Databricks Asset Bundles custom templates](https://www.linkedin.com/posts/mengyu-shi-175304129_databricks-dataengineering-platformengineering-share-7434206753027756033-KWzs).

## Core insight

Stop letting every new data project start with a blank page. DABs custom templates let you **define a company-standard project scaffold** that spins up fully configured repos in seconds — standardized folders, CI/CD, linters, and Dockerfiles included.

## Before vs After

| Dimension | ❌ Wild West | ✅ DABs Custom Templates |
|---|---|---|
| Project start | Copy-paste from old repo or blank page | `databricks bundle init my-company-template` |
| Folder structure | Inconsistent (src vs lib vs code) | Standard: tests, src, resources, fixtures |
| CI/CD | Missing or hand-configured each time | Pre-configured YAML (Actions / ADO) |
| Code quality | Forgotten linters, no hooks | Baked-in: ruff, pytest, pre-commit hooks |
| Containers | DIY Dockerfile or none | Standard Dockerfile for Container Services |
| Onboarding time | Days configuring boilerplate | Seconds — focus on business logic Day 1 |

## When to use this in this practice

- The DABs Data-Contract Golden Path subproject (`templates/dabs-data-product-template/`) **is** a custom template — `databricks-template-schema.json` declares the parameters captured by `databricks bundle init`.
- New product onboarding: `databricks bundle init <path-to-template>` produces a filled-in scaffold.
- Internal standardization: replace per-team-snowflake-projects with one template.

## Why standardization ≠ enforcement

Shi's framing: you're not adding rules; you're **removing friction**. Teams move faster when the guardrails are baked in. The template encodes opinions; engineers don't have to defend them per project.

## Cross-references

- `dabs-cicd-asset-bundles.md` — pairs with this for deployment after init.
- `metadata-driven-ingestion-framework.md` — Kocyigit's open-source framework follows this pattern.
- `../authored/dabs-data-contract-golden-path.md` — this practice's own custom template.
