"""Schema check — compares contract.schema against an actual table schema.

Used at deploy time and in DLT to fail loud on schema drift. Returns a
structured `SchemaCheckResult` so callers can format output for humans or
fail-fast in CI.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass
class SchemaCheckResult:
    """Outcome of a contract.schema vs actual-schema comparison."""

    contract_only: list[str] = field(default_factory=list)   # in contract, not in actual
    actual_only: list[str] = field(default_factory=list)     # in actual, not in contract
    type_mismatches: list[tuple[str, str, str]] = field(default_factory=list)
    nullability_mismatches: list[tuple[str, bool, bool]] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return not (
            self.contract_only
            or self.actual_only
            or self.type_mismatches
            or self.nullability_mismatches
        )

    def format(self) -> str:
        if self.is_clean:
            return "Schema check OK."
        lines = ["Schema check FAILED:"]
        if self.contract_only:
            lines.append(f"  Contract has columns missing from actual: {self.contract_only}")
        if self.actual_only:
            lines.append(f"  Actual has columns missing from contract: {self.actual_only}")
        for name, contract_t, actual_t in self.type_mismatches:
            lines.append(f"  Type mismatch on {name}: contract={contract_t}, actual={actual_t}")
        for name, contract_n, actual_n in self.nullability_mismatches:
            lines.append(f"  Nullability mismatch on {name}: contract.nullable={contract_n}, actual.nullable={actual_n}")
        return "\n".join(lines)


def run_schema_check(
    contract_columns: Iterable[dict[str, Any]],
    actual_columns: Iterable[dict[str, Any]],
) -> SchemaCheckResult:
    """Diff two column lists. Each column is a dict with at least:
        - name (str)
        - type (str)
        - nullable (bool)
    """
    c_by_name = {c["name"]: c for c in contract_columns}
    a_by_name = {a["name"]: a for a in actual_columns}

    result = SchemaCheckResult()

    result.contract_only = sorted(set(c_by_name) - set(a_by_name))
    result.actual_only = sorted(set(a_by_name) - set(c_by_name))

    for name in sorted(set(c_by_name) & set(a_by_name)):
        c, a = c_by_name[name], a_by_name[name]
        if c.get("type") != a.get("type"):
            result.type_mismatches.append((name, c.get("type", ""), a.get("type", "")))
        if c.get("nullable") != a.get("nullable"):
            result.nullability_mismatches.append((name, bool(c.get("nullable")), bool(a.get("nullable"))))

    return result
