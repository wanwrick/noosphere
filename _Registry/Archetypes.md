# Archetypes Registry

> Quick index of the 5 anonymized engagement archetypes codified in
> `initiatives/`. Each row maps to a full archetype dossier and a row in
> `initiatives/initiatives.yaml`. Forks should add their own engagements as
> additional rows in both places.

---

## Index

| ID | Codename | Sector | Type | Phase | Tier | Regulated | DPIA |
|----|----------|--------|------|-------|------|-----------|------|
| A | regulated-fsi-platform-launch | financial-services-regulated | platform-launch | build | T3 | yes | required |
| B | marketing-cdp-clean-room-modernization | financial-services-marketing | cdp-modernization | design | T2 | yes | required |
| C | self-serve-tenant-flatpack | financial-services-platform | self-serve-platform | build | T2 | yes | not required |
| D | agentic-self-serve-analytics | financial-services-analytics | agentic-analytics | design | T2 | yes | required |
| E | legacy-dw-to-cloud-lakehouse | financial-services-modernization | legacy-modernization | qualify | T3 | yes | required |

Phase ladder: `qualify → diagnose → design → build → embed → exit`.
Tier band: T1 (<$1M), T2 ($1M–$5M), T3 (>$5M) annual platform value.

---

## IP Coverage Matrix

Every archetype names ≥1 authored or curated IP file in `ip_applied`. This is
Invariant #1 from `CLAUDE.md`.

| Archetype | Authored IP | Curated IP |
|-----------|-------------|------------|
| A | No LAC, AI-Ready Platinum, Enterprise CLAUDE.md, DABs Golden Path, 10Q | Data Thinking 4P, Data Contracts, 5 Pillars, Bain 3-Layer, Metadata-Driven Ingestion |
| B | No LAC, DABs Golden Path | Dashboard Factory Escape, Data Contracts, Dataplex 6 Principles |
| C | Enterprise CLAUDE.md, DABs Golden Path, Platform-Mandate Playbook | DABs Custom Templates, DABs CI/CD, 5 Pillars |
| D | AI-Ready Platinum, No LAC, DABs Golden Path | Context Wall, Bain 3-Layer, Defending AI Spend 12Q |
| E | 10Q, No LAC, DABs Golden Path | 5 Pillars, CDO Top 10 |

---

## Governance Gate

Phase advance requires a `governance-audit` skill pass when the archetype has
`regulated: true` or any data product attached carries `pii: true`. Skill ships
in Phase 10. Until then, run the manual checklist in
`governance/regulated-fsi-compliance-runbook.md`.

---

## Files

- `initiatives/initiatives.yaml` — machine-readable registry, source of truth
- `initiatives/archetypes/ARCHETYPE-A-regulated-fsi-platform-launch.md`
- `initiatives/archetypes/ARCHETYPE-B-cdp-clean-room-modernization.md`
- `initiatives/archetypes/ARCHETYPE-C-self-serve-tenant-flatpack.md`
- `initiatives/archetypes/ARCHETYPE-D-agentic-self-serve-analytics.md`
- `initiatives/archetypes/ARCHETYPE-E-legacy-dw-to-cloud-lakehouse.md`
- `initiatives/CLAUDE.md` — routing for this directory

---

*Last updated: 2026-05-09 (v1.2.0 — initial Archetypes registry)*
