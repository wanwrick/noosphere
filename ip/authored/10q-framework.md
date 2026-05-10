# 10Q Framework — New Data Source Onboarding

> Use this **before** you build any new ingestion. Stress-test the source along 10 dimensions. The goal is to avoid 3 months of firefighting by surfacing the gotchas before pipeline design begins.

## When to use

- A new data source request lands in the producer team's queue.
- A consumer team proposes a new analytical use case that requires a new source.
- An existing source materially changes (new schema generation, new vendor system, new format).
- A migration is moving an existing source to a new platform.

## The 10 questions

| # | Dimension | What you are stress-testing |
|---|---|---|
| 1 | **Volume** | Cluster sizing · partition strategy · cost projection |
| 2 | **Freshness** | Real-time vs hourly vs daily — and what the consumer actually needs |
| 3 | **Schema** | Stability · evolution rules · rescue strategy |
| 4 | **Quality** | Acceptable null rates · business-rule violations · ownership of fixes |
| 5 | **Source Type** | Files · DB · API · Kafka · SaaS — drives ingestion pattern |
| 6 | **Incremental** | Watermark column · CDC · or full refresh? |
| 7 | **PII** | Which fields · masking spec · audit-logging expectations · residency |
| 8 | **Rate Limits** | Throttling · retry strategy · backoff design |
| 9 | **Replay** | Can we re-extract historical? Retention window? Idempotency? |
| 10 | **Gotchas** | Timezone · encoding · type mismatches · nested JSON · historical drift |

For the full elaboration of each question (questions to ask, why it matters, examples, red flags, recommended patterns), see `10q-toolkit/elicitation-guide.md`.

## The toolkit

| Artifact | Path | Audience |
|---|---|---|
| Stakeholder Intake Form | `10q-toolkit/stakeholder-intake-form.md` | Source owner / requesting team |
| Elicitation Guide | `10q-toolkit/elicitation-guide.md` | Producer engineer running the session |
| Intake Tracker Schema | `10q-toolkit/intake-tracker-schema.md` | Producer team — multi-source tracking |
| Miro Blueprint Spec | `10q-toolkit/miro-blueprint-spec.md` | Visual workshop facilitator |

## The discovery session

Default agenda — 90 minutes:

| Block | Duration | Purpose |
|---|---|---|
| Context | 10 min | Source owner explains the data; producer team listens |
| 10 questions | 60 min | Round-robin through the dimensions; producer drives, source owner answers |
| Cost projection | 10 min | Quick cost band per freshness option (real-time / hourly / daily / weekly) |
| Decision | 10 min | Go / no-go / send-back-with-questions |

If three or more questions return "not sure" or "we don't have that documented," the session ends as **send-back-with-questions**. Build does not begin until all 10 are answered.

## Output → pipeline design

The completed 10Q assessment maps directly into a `data-contract.yml` (see `dabs-data-contract-golden-path.md`):

| 10Q dimension | Contract field |
|---|---|
| Volume | `bronze.expected_volume`, `completeness.expected_row_count_min/max` |
| Freshness | `freshness.sla_minutes` |
| Schema | `schema.columns[]`, `bronze.schema_evolution` |
| Quality | `quality_expectations[]` |
| Source Type | `bronze.source_type` |
| Incremental | `bronze.ingestion_strategy`, `bronze.incremental_column` |
| PII | `schema.columns[].pii`, `schema.columns[].masking_function`, `metadata.pii` |
| Rate Limits | `bronze.rate_limit_aware` |
| Replay | `bronze.replay_window_days` (extension field) |
| Gotchas | inline comments in the contract YAML; logged in `_Logs/feedback.md` |

## Anti-patterns

- **Skipping 10Q "because the source team is in a hurry."** Three months of firefighting later: the source team is still in a hurry, and now the platform is too.
- **Filling in 10Q from documentation alone.** The session is the value; documentation lies. Get a human in the room.
- **Treating 10Q as a checklist.** It's an interview. Each "not sure" is a flag, not a row to skip.
- **No cost projection.** Without a cost band per freshness option, the freshness choice gets made by whoever speaks loudest.

## Verification

Before declaring 10Q complete:

- [ ] All 10 questions answered (no "not sure" responses).
- [ ] Cost band agreed by source owner + consumer.
- [ ] PII fields explicitly listed with masking_function per column.
- [ ] Replay strategy documented; retention window known.
- [ ] Output landed in the intake tracker (`10q-toolkit/intake-tracker-schema.md`).
- [ ] Decision recorded: GO / NO-GO / SEND BACK.

## Cross-references

- `dabs-data-contract-golden-path.md` — the contract YAML the 10Q feeds.
- `no-lac-principle.md` — the No LAC posture argues for *almost everything* in Bronze; 10Q decides which "almost."
- `../curated/data-contracts-producer-consumer.md` — Baeyens's contract pattern is what 10Q output flows into.
- `../curated/metadata-driven-ingestion-framework.md` — Kocyigit's framework is what consumes the 10Q output as YAML metadata.
- `Workflows/new-data-source-intake.md` — the operational workflow that runs 10Q + downstream.

---

*Owned by: producer-side data engineering lead. Run for every new data source intake.*
