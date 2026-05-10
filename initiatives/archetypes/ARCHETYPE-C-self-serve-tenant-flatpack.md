# ARCHETYPE-C — Self-Serve Tenant Flatpack

> **Pattern:** "IKEA flatpack" toolkit for tenant + data-exchange provisioning. Any new domain team can stand up a compliant tenant + onboard their first data product in days, not months.

## When this archetype fits

- Producer-side platform team is being asked to provision tenants for many domain teams.
- Self-serve is the goal but the setup work is bespoke per tenant.
- The org is shifting from "IT provisions everything" to "platform provides primitives; teams self-serve."

## The flatpack

A standardized toolkit:

| Component | What's included |
|---|---|
| Tenant Terraform module | Workspaces · catalogs · grants · cluster policies · network attachments |
| DABs Custom Template | The Data-Contract Golden Path subproject (see `templates/dabs-data-product-template/`) |
| Onboarding playbook | Step-by-step for the new domain team |
| Validation gate | `validate_bundle.sh` 6-check + governance-audit skill |
| Operating cadence kit | Monday producer ritual + DQ alerting + cost dashboard |

Domain teams clone the template; fill in their `data-contract.yml`; run two commands; ship.

## Phases

| Phase | What happens |
|---|---|
| Qualify | Domain teams' on-deck list; first 3 candidates picked |
| Diagnose | Current tenant-provisioning friction inventory (cycle time, manual steps, error rate) |
| Design | The flatpack components (above); convention-over-configuration choices documented |
| Build | First domain end-to-end; second domain proves repeatability |
| Embed | Documentation + training + office hours; rotation model for platform team |
| Exit | Producer team supports flatpack; domain teams own their tenants |

## IP applied

| IP | Role |
|---|---|
| `enterprise-claude-md.md` (authored) | Per-tenant CLAUDE.md baseline |
| `dabs-data-contract-golden-path.md` (authored) | The forkable data-product template |
| `platform-mandate-playbook.md` (authored) | Producer-team mandate framing if formalization is needed |
| `dabs-custom-templates.md` (curated, Shi) | The `databricks bundle init` pattern |
| `dabs-cicd-asset-bundles.md` (curated, Shi) | Two-command CI/CD |
| `data-product-architecture-5-pillars.md` (curated, Czarnas) | Pillar 4 (Standard Templates) is the headline |

## Regulatory pattern

OSFI-style. DPIA usually not required *for the toolkit itself*; required *per tenant onboarding* depending on the data the tenant ingests.

## Operating cadence

- **Weekly:** Producer-team office hours for domain teams.
- **Bi-weekly:** Flatpack improvement queue review (what should ship in v+1?).
- **Monthly:** Onboarding velocity review (how many domains? cycle time? friction points?).

## Common gotchas

- Building too many toggles into the template. Convention over configuration. *80% solution that ships > 100% solution that doesn't.*
- Skipping the office-hours step. Self-serve without support is *abandoning*, not *enabling*.
- Versioning the template casually. The template is now an internal product; treat it like one.
- Letting domain teams hand-edit the bundle. They should fork; the platform team owns the template.

## Cross-references

- `../initiatives.yaml` row id `ARCHETYPE-C-…`
- `../../templates/dabs-data-product-template/README.md`
- `../../ip/authored/dabs-data-contract-golden-path.md`
- `../../ip/curated/dabs-custom-templates.md`
