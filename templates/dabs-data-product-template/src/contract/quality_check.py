"""Quality-expectation check — translates contract quality_expectations[]
into DLT-style expectation specs.

Decouples the contract from the runtime: this module produces
implementation-agnostic specs; src/pipelines/silver.py consumes them and
emits actual `@dlt.expect_*` decorators.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass
class QualityCheckResult:
    """Outcome of compiling contract.quality_expectations[] into DLT specs."""

    specs: list[dict[str, str]]   # list of {name, expectation, on_violation}
    errors: list[str]

    @property
    def is_clean(self) -> bool:
        return not self.errors


_VALID_VIOLATIONS = {"fail", "drop", "drop_to_quarantine", "warn"}


def run_quality_check(
    expectations: Iterable[dict[str, Any]],
) -> QualityCheckResult:
    """Validate + normalize quality_expectations[] from a contract."""
    specs: list[dict[str, str]] = []
    errors: list[str] = []

    for i, exp in enumerate(expectations):
        if not isinstance(exp, dict):
            errors.append(f"Expectation #{i} is not a dict.")
            continue
        name = exp.get("name", "")
        expr = exp.get("expectation", "")
        on_v = exp.get("on_violation", "")
        if not name or not expr:
            errors.append(f"Expectation #{i} missing name or expectation.")
            continue
        if on_v not in _VALID_VIOLATIONS:
            errors.append(
                f"Expectation '{name}' has invalid on_violation={on_v!r}; "
                f"must be one of {sorted(_VALID_VIOLATIONS)}."
            )
            continue
        specs.append({"name": name, "expectation": expr, "on_violation": on_v})

    return QualityCheckResult(specs=specs, errors=errors)


def to_dlt_decorator_name(on_violation: str) -> str:
    """Map an on_violation value to its DLT decorator name."""
    return {
        "fail": "expect_or_fail",
        "drop": "expect_or_drop",
        "drop_to_quarantine": "expect_or_drop",   # quarantine handled at table level
        "warn": "expect",
    }[on_violation]
