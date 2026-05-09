# 10Q — Stakeholder Intake Form

> Form-style intake for source owners. Fill **before** the discovery session. Producer team uses your answers to drive the agenda.

**Source name:** _[plain English label]_
**Source owner / team:** _[team name]_
**Primary contact (name / role):** _[name + role]_
**Date submitted:** _[YYYY-MM-DD]_
**Use case in one sentence:** _[what business question this source answers]_

---

## 1. Volume

- Current data size (GB / TB):
- Daily growth rate:
- Retention period (months / years):
- Peak burst rate (if known):

## 2. Freshness

- Latency requirement (real-time / near-real-time / hourly / daily / weekly):
- What goes wrong at the next-slower latency tier?
- Who consumes this and when (which dashboards, which agents, which decisions)?

## 3. Schema

- Schema registry / contract (URL or "none"):
- Stability — never / rarely / often / constantly:
- Backwards-compatibility commitment from source team — yes / no:
- Change notification mechanism — yes / no / sometimes:

## 4. Quality

- Known quality issues (free text):
- Acceptable null rate per critical field:
- Business rules to validate (amounts > 0, dates in range, …):
- Quality owner at the source:

## 5. Source type

- Mark one: Cloud files (S3/ADLS/GCS) · Database (with version) · REST API · Kafka / Event Hubs · SaaS connector · Other:
- Auth method (API key / OAuth / Service account / Cert):
- Documentation URL:

## 6. Incremental

- Incremental column (if any):
- CDC support — yes / no / partial:
- Updates can mutate history — yes / no:
- "Full refresh nightly" acceptable — yes / no:

## 7. PII

- PII fields (list each):
- Sensitivity classification per field (public / internal / confidential / restricted):
- Encryption-at-rest required — yes / no:
- Masking / tokenization expectations:
- Data residency constraints:

## 8. Rate limits

- Requests per second / minute / day:
- Concurrent connection limit:
- Burst handling expectation:
- Off-peak window for heavy extraction:

## 9. Replay

- How long is source data retained?
- Replay from a checkpoint or timestamp — yes / no:
- Backfill window (days):
- Idempotency on retry — yes / no:

## 10. Gotchas

- Timezone conventions:
- Encoding (UTF-8 / Latin-1 / Windows-1252):
- Known type mismatches:
- Nested JSON depth:
- Historical drift / quality changes over time:

---

## Submitter sign-off

- [ ] All sections answered to the best of my knowledge.
- [ ] I understand "not sure" answers will trigger send-back-with-questions.
- [ ] I have authority to commit my team to data quality and freshness obligations described above.

**Submitter:** _[name]_   **Date:** _[YYYY-MM-DD]_
