# No LAC — *No Lack of Analytical Capability*

> **Mantra:** *Land it once. Land it well. Get out of the business's way.*

A platform's job is **not** to gatekeep, sequence, or curate the analytical questions the business is allowed to ask. Its job is to make the data available so the business can ask any analytical question and get a defensible answer fast.

No LAC is a **humility principle** as much as a technical one: it asserts that the platform team does not know in advance which questions matter most, so the platform must be built to make every plausible question answerable.

---

## Why "No LAC" not "No Lag"

"No Lag" is a marketing claim about latency. "No LAC" is an architectural commitment about *capability*.

| Posture | What the platform team optimizes for |
|---|---|
| ❌ Lag-first thinking | Time from raw to ready. Latency theatre. Real-time-ness as a vanity metric. |
| ✅ LAC-first thinking | The set of questions the business can answer without filing a ticket. Capability surface area. Self-serve with safety. |

A platform can have low lag and still leave the business unable to answer its real questions. That is failure. A platform with one-day Bronze freshness but every plausible analytical question answerable across the lakehouse is success.

---

## The six operational stances

1. **Bronze ingests almost everything plausibly needed for analytics.** Full schema, full row depth, full history where the source allows. *Almost* everything because intellectual humility — ingestion has cost and obligation, and not every byte deserves a permanent home. The producer team commits to landing every column the business is plausibly going to want, not just the ones requested today.
2. **Source-system access is a one-time event per source, not a recurring cost.** The pipeline does not return to the source to answer new questions. Re-ingestion exists only to fix correctness, not to widen scope.
3. **Bronze → Silver → Gold → Platinum iterates fast precisely because data is already landed.** New analytical questions translate to new Silver/Gold transformations, not new ingestion projects. Time-to-insight is a transformation problem, not an integration problem.
4. **Custom code lives only at Gold.** Bronze and Silver are reusable patterns parameterized by metadata; the first place a domain expresses opinion is the first cross-source join. This protects pipeline iteration speed.
5. **The business has full analytical capability over Platinum.** Self-serve reads. Agentic reads (per AI-Ready Platinum Layer). The platform's value is measured by *how out of the way it stays* once a data product is landed and contracted.
6. **The best analytical insights come from the business, not the platform team.** The platform is a public utility, not an oracle. Empowerment over gatekeeping.

---

## The Atomic Framework — medallion architecture

```
+-----------+   +-----------+   +-----------+   +-----------+   +-----------+   +-----------+
|  BRONZE   |-->|  SILVER I |-->| SILVER II |-->|SILVER III |-->|   GOLD    |-->| PLATINUM  |
+-----------+   +-----------+   +-----------+   +-----------+   +-----------+   +-----------+
| Land data | | Clean &     | | Denormalize | | SCD Type 2  | | Cross-     | | Semantic + |
| as-is. One| | standardize.| | within      | | historicals.| | source     | | AI-ready   |
| reusable  | | One code    | | source.     | | No cross-   | | joins.     | | scoped     |
| framework | | base reused | | Same-source | | source      | | Derived &  | | views + UC |
| per file  | | for every   | | joins only. | | joins yet.  | | calculated | | Functions. |
| type.     | | domain.     | | Optional.   |   +-----------+   | fields.    |   +-----------+
| Self-     | | Only param  |   +-----------+                   | CUSTOM     |   Power BI ·
| healing   | | files       |                                     | CODE       |   AI/BI ·
| jobs.     | | change.     |                                     | LIVES HERE |   Claude · Agents
+-----------+   +-----------+                                     | ONLY.      |
                                                                  +-----------+
```

| Layer | Property | Why it matters |
|---|---|---|
| **Bronze** | Append-only · explicit schema · framework-per-file-type | Audit-grade lineage; immutability; reusable across all domains |
| **Silver I** | Clean + standardize within source · single code base | One Silver-I codebase serves every domain; only YAML/parameter files change |
| **Silver II** | Optional denormalization within source | Reduces table count where useful; never crosses sources |
| **Silver III** | SCD Type 2 historicals | Time-travel without bespoke engineering; applies uniformly |
| **Gold** | First cross-source join · derived/calculated fields | The **only** layer where domain opinion lives in custom code |
| **Platinum** | Semantic layer · AI-ready scoped views · UC Functions | Single publish; multiple consumers (BI + agents). See `ai-ready-platinum-layer.md` |

### Custom code at Gold only

This is the load-bearing rule. If domains can write custom code in Silver, every domain reinvents Bronze→Silver patterns and Bronze loses its no-lag iteration property. The discipline of pushing custom code to Gold protects the pipeline iteration speed that the LAC principle promises.

### Cloud-agnostic outputs

Gold and Platinum tables are written in **Delta** format on cloud object storage. They are consumable directly from BigQuery via federation, from Snowflake via external tables, from any Iceberg-compatible reader. The lakehouse is the publication layer; the consumer's compute is their choice.

---

## Intellectual humility — what "almost everything" means

"Bronze ingests almost everything plausibly needed for analytics" is deliberately not "Bronze ingests everything." Three caveats:

1. **Not every byte deserves a permanent home.** Logs, ephemeral telemetry, derived intermediates from external systems — these may not warrant Bronze residency. Make the choice deliberately.
2. **Privacy + retention obligations narrow the surface.** PII data with strict retention windows (PIPEDA-style erasure obligations, GDPR Article 17) belongs in Bronze only if you can honor the retention contract. If you cannot, stay out.
3. **Cost discipline is real.** Storage is cheap; compute on storage is not. Bronze tables that nobody ever reads are negative-value assets. Periodic FinOps review (`Workflows/monday-producer-ritual.md`) prunes the surface.

The principle is *capability without bottleneck*, not *hoarding for hoarding's sake*.

---

## Applied-in-phase map

| Initiative phase | Which No LAC stance applies |
|---|---|
| Qualify | #1 — write down which sources should land in Bronze and why |
| Diagnose | #1 + #2 — confirm one-time-source-access; map known gotchas (10Q output) |
| Design | #4 — confirm Silver is parameterized; custom code only at Gold |
| Build | #3 — measure iteration speed Silver → Gold → Platinum |
| Embed | #5 — measure self-serve read patterns; close adoption gap |
| Exit | #6 — handoff posture: business owns analytical authority |

---

## Anti-patterns

- **Custom Spark code in Silver.** Silver is supposed to be one codebase reused across all domains. Domain-specific Silver code is a smell.
- **Going back to the source for every new analytical question.** That is integration debt expressed as latency.
- **Platinum tables with no AI Consumption Contract.** See `ai-ready-platinum-layer.md`.
- **Bronze schemas that change shape without rescue columns.** Use `_rescued_data` for unknown fields; fail loud, not silent.

---

## Verification checklist

Before declaring a data product No-LAC-compliant:

- [ ] Bronze has explicit schema; no auto-detection.
- [ ] Silver code is parameterized — no domain-specific custom logic.
- [ ] Gold is the only place custom code lives.
- [ ] Platinum has both BI and AI consumption interfaces (per AI-Ready Platinum).
- [ ] Source access happened once at onboarding (10Q assessment); no recurring source pulls for new questions.
- [ ] Iteration speed Silver → Platinum is < 1 sprint for new transformations.
- [ ] Business has self-serve read access to Platinum (UC ABAC + grants verified).

---

## Cross-references

- `ai-ready-platinum-layer.md` — Principle 4: Platinum is dual-interface (BI + agents).
- `10q-framework.md` — onboarding stress-test confirms Bronze comprehensiveness.
- `dabs-data-contract-golden-path.md` — the Atomic Framework rendered as a working DABs subproject.
- `../curated/data-product-architecture-5-pillars.md` — Czarnas's "boundaries first" pillar matches stance #4.
- `../curated/metadata-driven-ingestion-framework.md` — Kocyigit's YAML-as-source-of-truth matches stance #4.
- `../curated/data-contracts-producer-consumer.md` — Baeyens's contract pattern is what makes Platinum reads safe.

---

## Diagram

See `_Diagrams/no-lac-architecture.md` for the Mermaid rendering of the medallion flow.

---

*Owned by: the producer team lead. Reviewed: every minor version of the practice OS.*
