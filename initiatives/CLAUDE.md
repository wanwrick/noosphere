# Initiatives — Routing

5 anonymized engagement archetypes. Forks should add their own archetypes as new files; the existing five are ready-to-use templates.

| File | Pattern |
|---|---|
| `initiatives.yaml` | Registry: each archetype as a row with phase, IP applied, governance status |
| `archetypes/ARCHETYPE-A-regulated-fsi-platform-launch.md` | Bronze→Platinum on lakehouse · regulated reporting · secure tenant model |
| `archetypes/ARCHETYPE-B-cdp-clean-room-modernization.md` | Marketing modernization · CDP integration · governed clean rooms |
| `archetypes/ARCHETYPE-C-self-serve-tenant-flatpack.md` | Self-serve provisioning · "IKEA flatpack" toolkit · Tenants + Exchange |
| `archetypes/ARCHETYPE-D-agentic-self-serve-analytics.md` | Semantic layer + AI/BI Genie + agentic analytics pilot |
| `archetypes/ARCHETYPE-E-legacy-dw-to-cloud-lakehouse.md` | Legacy DW → cloud lakehouse migration |

Every archetype carries `ip_applied` referencing one or more authored / curated IP files. The `governance-audit` skill enforces phase advance only when DPIA + classification + masking obligations are met (per `compliance-register.yaml`).
