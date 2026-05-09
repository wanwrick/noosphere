---
name: data-source-10q-intake
description: Run the 10Q onboarding interview for a new data source. Produces a complete intake brief that drives the metadata-driven ingestion pipeline (DABs Golden Path) and the AI-Ready Platinum publish layer. Use when a new producer is being onboarded, when a source is being re-platformed, or when a data contract needs to be authored from a vague request.
---

# data-source-10q-intake

You are running the **10Q intake interview**: the 10 questions that turn a
fuzzy "we need this data" request into a deployable data contract.

## Source IP
- Authored: `ip/authored/10q-framework.md` (canonical 10 questions).
- Authored: `ip/authored/10q-toolkit/` (templates, intake scripts).
- Authored: `ip/authored/dabs-data-contract-golden-path.md` (where the
  intake output lands).
- Curated: `ip/curated/metadata-driven-ingestion-framework.md` (Mahboub).

## When to invoke
- "Onboard a new source", "intake this dataset", "draft a data contract".
- A producer-consumer conversation with no governance, no SLA, no schema.

## The 10 Questions (ask in order)
1. **Who is the producer?** Domain, team, accountable owner, business
   contact. Not the IT contact.
2. **Who are the consumers?** Names of the AI agents, dashboards, models
   downstream. If unknown, stop — there is no data product yet.
3. **What is the use case?** One sentence. If it takes a paragraph, it is
   two use cases.
4. **What is the source system?** Type, version, change-data-capture
   support, freshness floor.
5. **What is the schema?** Columns, types, primary key, business key,
   foreign keys. Pull from source if available.
6. **What is the classification?** PII / PCI / financial / public.
   CDMC-aligned 4-tier (`governance/client-data-classification.md`).
7. **What are the quality expectations?** Null tolerance, uniqueness,
   referential integrity, freshness SLA, volume bounds.
8. **What are the access requirements?** Who reads Bronze / Silver /
   Platinum. UC ABAC tags (`ip/authored/ai-ready-platinum-layer.md`).
9. **What is the retention obligation?** GDPR Article 17, regulated
   retention, archival path. Cross-ref `governance/compliance-register.yaml`.
10. **What is the AI consumption pattern?** Agentic read / RAG / fine-tune /
    feature store. Determines Platinum view shape.

## Output shape
A `data-contract.yml` populated against the schema in
`templates/dabs-data-product-template/data-contract.schema.json`. Plus a
two-page intake brief:
1. Producer + consumers + use case (BLUF).
2. Schema + classification + DQ expectations.
3. Access matrix + retention + AI consumption.
4. Open questions / DPIA triggers / governance gates.
5. Recommended next step (DABs init, governance audit, etc.).

## Verification
- All 10 questions answered or marked `unknown` with an owner + due date.
- Classification answer drives PII masking declaration in the contract.
- If `regulated: true` → trigger `governance-audit` skill before any
  deployment.
- BLUF check: first sentence of the brief states the producer, consumer,
  and use case in ≤25 words.

## Handoff
- Save brief to `data-products/<domain>-<dataset>-intake.md`.
- Save contract to `data-products/<domain>-<dataset>/data-contract.yml`.
- Append the new product to `data-products/data-products.yaml`.
- If first time onboarding → run `dabs-template-init` skill next.
