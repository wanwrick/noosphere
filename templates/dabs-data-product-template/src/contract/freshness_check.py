"""Freshness check — verifies last-ingested timestamp against contract SLA."""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass


@dataclass
class FreshnessCheckResult:
    """Outcome of a freshness assertion."""

    sla_minutes: int
    observed_lag_minutes: float
    is_within_sla: bool

    def format(self) -> str:
        verb = "PASS" if self.is_within_sla else "FAIL"
        return (
            f"Freshness {verb}: observed_lag={self.observed_lag_minutes:.1f}min, "
            f"sla={self.sla_minutes}min."
        )


def run_freshness_check(
    last_ingest_ts: dt.datetime,
    sla_minutes: int,
    now: dt.datetime | None = None,
) -> FreshnessCheckResult:
    """Compute lag = now - last_ingest_ts; compare to SLA.

    Args:
        last_ingest_ts: timezone-aware datetime of the most recent successful ingest.
        sla_minutes: contract.freshness.sla_minutes value.
        now: override for testability; defaults to UTC now.

    Returns:
        FreshnessCheckResult with the verdict.
    """
    if now is None:
        now = dt.datetime.now(dt.timezone.utc)
    if last_ingest_ts.tzinfo is None:
        last_ingest_ts = last_ingest_ts.replace(tzinfo=dt.timezone.utc)
    lag = (now - last_ingest_ts).total_seconds() / 60.0
    return FreshnessCheckResult(
        sla_minutes=sla_minutes,
        observed_lag_minutes=lag,
        is_within_sla=lag <= sla_minutes,
    )
