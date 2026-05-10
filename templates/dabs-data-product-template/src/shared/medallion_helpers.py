"""Shared utilities used by every Medallion layer."""

from __future__ import annotations

from typing import Any


def table_name(contract: dict[str, Any], layer: str) -> str:
    """Conventional table name: <metadata.id>_<layer>."""
    valid = {"bronze", "silver", "gold", "platinum"}
    if layer not in valid:
        raise ValueError(f"layer must be one of {valid}; got {layer!r}")
    return f"{contract['metadata']['id']}_{layer}"


def schema_name(contract: dict[str, Any], catalog: str) -> str:
    """Fully-qualified schema name for a given Medallion layer."""
    return f"{catalog}.{contract['metadata']['id']}"


def explicit_schema_ddl(contract: dict[str, Any]) -> str:
    """Build a Spark DDL string from contract.schema.columns[]."""
    cols = contract.get("schema", {}).get("columns", [])
    parts = []
    for c in cols:
        nullability = "" if c.get("nullable", True) else " NOT NULL"
        parts.append(f"{c['name']} {c['type']}{nullability}")
    return ", ".join(parts)
