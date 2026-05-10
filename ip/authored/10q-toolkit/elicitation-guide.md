# 10Q — Elicitation Guide

> Facilitator's guide for the producer engineer running the 10Q discovery session. For every dimension: questions to ask, why it matters, examples, red flags, recommended patterns.

## How to run the session

- 90 minutes, video + screen share.
- Source owner + producer engineer + (optional) consumer-team observer.
- One scribe.
- Producer drives. Source owner answers.
- "Not sure" is a flag, not a fail — log it and circle back.

---

## 1. Volume

**Questions:** Current size (GB/TB)? Daily / hourly growth rate? Retention period? Peak burst?

**Why it matters:** Drives cluster sizing + partitioning + storage cost.

**Examples:**
- 500 GB current, +10 GB/day, 2-year retention → ~7.3 TB total → partition by date; autoscaling clusters.

**Red flags:** "Not sure" on volume. Assuming today's volume will stay small. Vendor benchmark numbers without ground truth.

**Patterns:** Partition by date (most common). Z-order on high-cardinality filter columns. Cluster autoscaling tuned to 80th-percentile load.

---

## 2. Freshness

**Questions:** Real-time / hourly / daily / weekly? What breaks at the next-slower tier? Who consumes and when?

**Why it matters:** Real-time is ~10–25x cost of daily batch. Wrong choice burns budget or misses SLA.

**Cost bands (illustrative):**

| Tier | Latency | Pattern |
|---|---|---|
| Real-time | <1 min | Structured Streaming · 24/7 cluster |
| Near real-time | <15 min | Structured Streaming · scheduled batch |
| Hourly batch | <1 hr | DLT · scheduled |
| Daily batch | <24 hr | DLT · scheduled |
| Weekly | <7 days | DLT · cron weekly |

**Red flags:** "As fast as possible" with no clear consumer justification. Building real-time for daily decisions. 24/7 clusters for daily loads.

**Patterns:** Default to one tier slower than asked; ask the consumer to defend the tier with a decision SLA.

---

## 3. Schema

**Questions:** Registry / contract URL? Stability — never / rarely / often / constantly? Backwards-compat commitment? Change notifications?

**Why it matters:** Determines schema evolution strategy and validation depth.

| Stability | Recommended pattern |
|---|---|
| Stable | Strict schema enforcement |
| Changing | Allow evolution + rescued-data column |
| Unknown | Schema-on-read + rescued-data column |

**Red flags:** No registry. No change-notification mechanism. Source team unwilling to commit to backwards-compat.

**Patterns:** Always reserve a `_rescued_data` column at Bronze. Fail loud (DLT expectation) on schema drift, never silent.

---

## 4. Quality

**Questions:** Acceptable null rate per critical field? Business rules (amounts > 0, dates in range)? Known quality issues by period or domain? Quality owner at source?

**Why it matters:** Sets consumer expectations. Drives Bronze → Silver validation rules.

**Example thresholds:**

| Field | Threshold |
|---|---|
| Customer email | <5% nulls |
| Transaction amount | 0% null AND > 0 |
| Order date | within last 30 days |

**Red flags:** "All data is high quality" with no metrics. No quality owner at source. Quality-issue stories that surface in conversation but aren't documented.

**Patterns:** Document thresholds in `quality_expectations[]` of the data contract. Quarantine, never drop. Alert on threshold breach.

---

## 5. Source type

**Questions:** Files / database / API / Kafka / SaaS? Auth? Documentation URL?

| Source | Recommended pattern | Complexity |
|---|---|---|
| Cloud files (S3/ADLS/GCS) | Auto Loader | Low |
| Database (Postgres/MySQL/SQL Server) | JDBC or CDC | Medium |
| REST API | Custom client + Auto Loader | High |
| Message queue (Kafka/Event Hubs/Pub/Sub) | Structured Streaming | High |
| SaaS (Salesforce/Workday/HubSpot) | Native connector / Fivetran / Airbyte | Medium |

**Red flags:** Custom auth flows. APIs without pagination. SaaS connectors not in vendor catalogs.

**Patterns:** Cloud files → Auto Loader is the cheapest, safest default. Always land files first; ingest from files.

---

## 6. Incremental

**Questions:** Incremental column? CDC support? Updates mutate history? Reliability of the watermark?

**Why it matters:** Avoid scanning 100% of a large table every run. 90%+ cost reduction routinely.

| Method | Best for |
|---|---|
| Timestamp watermark (`updated_at`) | Most databases — simple, reliable |
| CDC | High-volume, captures deletes |
| Full refresh only | Last resort for small tables |

**Red flags:** "We don't have an updated_at column." Watermarks that aren't monotonically increasing. Updates that mutate history without a versioning column.

**Cost example (1 TB table):** Hourly full refresh ~$4,800/day vs incremental 10 GB/hr ~$120/day — 97% cheaper.

**Patterns:** Lakeflow Connect query-based incremental for sources without CDC. Default to incremental; full refresh only when justified.

---

## 7. PII

**Questions:** Which fields exactly? Encryption-at-rest? Masking / tokenization? Audit-logging? Residency?

**Why it matters:** Regulator-grade risk. Misclassification = regulatory finding.

**Pattern by Medallion layer:**

| Layer | PII handling |
|---|---|
| Bronze | Encrypt at rest · strict access controls · audit log every read |
| Silver | Apply masking functions per UC tag |
| Gold | Aggregate or exclude PII where possible |
| Platinum | PII never in scoped agent views unless masked |

**Red flags:** "We don't have PII." (You almost always do.) "We'll handle masking later." (Later never comes.) PII fields without per-column masking_function.

**Patterns:** UC tags + masking functions (per `playbooks/governance/masking-functions-pattern.md`). Restricted-class data only in secure tenants.

---

## 8. Rate limits

**Questions:** Requests/sec, requests/day, burst limits? Concurrent connection cap?

**Patterns:** Exponential backoff. Request batching. Off-peak scheduling. Pre-negotiated extraction window.

**Red flags:** "We'll figure it out." Rate limits documented in chat threads, not in API docs.

---

## 9. Replay

**Questions:** Source data retention? Replay from checkpoint / timestamp? Idempotency on retry?

**Patterns:**

| Source type | Replay |
|---|---|
| Immutable (files, Kafka) | Easy replay |
| Mutable (databases) | Historical state may be lost |
| APIs with retention | Limited window (e.g., 7 days) |

**Red flags:** No retention SLA from source team. Source overwrites without versioning.

---

## 10. Gotchas

**Questions:** Timezone? Encoding? Type mismatches? Nested JSON? Historical drift?

| Gotcha | Mitigation |
|---|---|
| Timezones / DST | Normalize to UTC at Bronze; convert at Gold |
| Encoding (UTF-8 vs Latin-1 vs Win-1252) | Force UTF-8 on ingest; validate at Silver |
| Type mismatches (numbers as strings) | Cast + validate at Silver; rescue bad rows |
| Nested JSON | Flatten at Silver; rescue inconsistent nesting |
| Historical drift | Separate backfill validation from incremental |

**Red flags:** Source claims "no gotchas." (There are always gotchas.)

---

## Quick-summary template (post-session, paste into Slack / Doc)

```
DATA SOURCE: [name]

CHARACTERISTICS
- Volume: [size], [growth]/day
- Freshness: [tier]
- Schema: [stability]
- Quality: [clean/messy/unknown]

SOURCE
- Type: [files/db/api/kafka/saas]
- Incremental: [yes (timestamp)/yes (cdc)/no]
- Rate limits: [...]

SECURITY
- Auth: [...]
- PII: [yes: <list>/no]
- Encryption: [yes/no]

OPERATIONS
- Replay: [yes (window)/limited/no]
- SLA: [99.9%/99%/best-effort]
- Gotchas: [...]

DECISION
- Recommended: [Auto Loader / JDBC / Streaming / ...]
- Architecture: [batch / streaming / micro-batch]
- Strategy: [filter by updated_at / CDC / full refresh]
- Quality: [strict / rescue / quarantine]
- Security: [mask in Silver / encrypt at rest]
- Monitoring: [alerts on lag > X / null rate > Y%]

GO / NO-GO / SEND BACK: [decision]
```

---

## After the session

1. Producer engineer fills in the corresponding `data-contract.yml` (see DABs Golden Path subproject).
2. Output lands in the intake tracker (`intake-tracker-schema.md`).
3. Decision is logged in `Knowledge/Decisions/`.
4. If GO: enter Design phase. If NO-GO: archive. If SEND BACK: schedule follow-up with specific outstanding questions.
