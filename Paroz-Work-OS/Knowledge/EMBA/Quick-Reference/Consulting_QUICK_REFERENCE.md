# Consulting — QUICK REFERENCE
## Professional Resource Collection

---

## Data Platform Migration (5 Phases)

```
Phase 1A: Problematic reports → Databricks Gold.Legacy
Phase 1B: Working reports stay in EDW, parallel Databricks build
Phase 2:  Move upstream, remove EDW dependency
Phase 3:  Refactor to Gold.Medallion (semantic layer)
Phase 4:  EDW decommission → fully on Databricks
Phase 5:  Gold.Legacy decommission → fully on Gold.Medallion
```

---

## Domain Architecture

| Domain Type | Owner | Purpose |
|------------|-------|---------|
| **Business Capability** | SW Engineering Squads | Microservice-scoped data |
| **Data Domain** | CLP / Data Engineering | Enterprise data model across journeys |
| **Department Domain** | Data Engineering + Department | Datamarts for specific dept use cases |

---

## Folder Contents

| Resource | Type |
|----------|------|
| Scratch Pad (1).pdf | Data platform migration architecture |
| Visa US session files | Session notes (.docx) |
| McKinsey/ | Research screenshots |
| SlideSalad templates | Presentation templates (.pptx/.pdf) |
| Industry screenshots | Consulting firm research (.png) |

---

**Folder:** `Smith Cornell EMBA Classes/Consulting/`
**SKILL File:** `EMBA-Code-Reference/context/Consulting.SKILL.md`
