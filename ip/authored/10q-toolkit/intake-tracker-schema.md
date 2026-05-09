# 10Q — Intake Tracker Schema

> Schema for a multi-source pipeline intake tracker. Implement as a Google Sheet, Airtable base, or — better — a Notion database backed by the registries in `initiatives/`.

## Columns

| Column | Type | Notes |
|---|---|---|
| `intake_id` | string (auto) | Format: `INTAKE-YYYY-NNNN` |
| `source_name` | string | Plain-English label |
| `source_owner_team` | string | Team / person |
| `submitted_date` | date | When the form arrived |
| `requesting_team` | string | Consumer team |
| `use_case_one_liner` | string | Business question this serves |
| `decision` | enum | `pending` · `go` · `no-go` · `send-back` |
| `decision_date` | date | When the decision was logged |
| `decision_owner` | string | Producer engineer who decided |
| `q1_volume_score` | enum | `green` · `amber` · `red` · `unknown` |
| `q2_freshness_score` | enum | … |
| `q3_schema_score` | enum | … |
| `q4_quality_score` | enum | … |
| `q5_source_type_score` | enum | … |
| `q6_incremental_score` | enum | … |
| `q7_pii_score` | enum | … |
| `q8_rate_limits_score` | enum | … |
| `q9_replay_score` | enum | … |
| `q10_gotchas_score` | enum | … |
| `red_flag_count` | int | Auto-computed: count of `red` in q1-q10 |
| `unknown_count` | int | Auto-computed: count of `unknown` in q1-q10 |
| `cost_band` | enum | `T1: <$200/mo` · `T2: $200-2k/mo` · `T3: $2k-10k/mo` · `T4: >$10k/mo` |
| `freshness_tier_chosen` | enum | `realtime` · `near-realtime` · `hourly` · `daily` · `weekly` |
| `pii_classification` | enum | `none` · `internal` · `confidential` · `restricted` |
| `target_archetype_id` | string | Link to `initiatives/archetypes/` (e.g., `ARCHETYPE-A`) |
| `data_contract_path` | string | Path to the `data-contract.yml` once drafted |
| `target_quarter` | string | When build is scheduled |
| `notes` | text | Free-form |

## Decision rules

- `go` requires red_flag_count == 0 AND unknown_count == 0.
- `send-back` if red_flag_count > 0 OR unknown_count > 2.
- `no-go` if cost_band > business value (justify in notes).

## Views

| View | Filter |
|---|---|
| Active intake queue | `decision == pending` |
| Send-back follow-ups | `decision == send-back` AND submitted_date > 30 days ago |
| Recent GO | `decision == go` AND decision_date last 90 days |
| PII watch | `pii_classification IN ('confidential', 'restricted')` |
| Cost watch | `cost_band IN ('T3', 'T4')` |

## Reporting

Weekly producer ritual (`Workflows/monday-producer-ritual.md`) reviews:
1. Active intake queue depth.
2. Send-back follow-ups aging > 14 days.
3. Recent GO decisions: status of contract drafting.
