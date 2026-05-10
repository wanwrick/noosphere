"""Contract loader — parses + validates data-contract.yml against the schema.

Single entry point: `load(path) -> dict`. Returns the parsed contract as a
plain Python dict; raises `ContractError` on any validation failure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import ValidationError as _JsonSchemaError
except ImportError as exc:                # pragma: no cover
    raise ImportError(
        "jsonschema is required: pip install jsonschema>=4.18"
    ) from exc

_HERE = Path(__file__).resolve().parent          # src/contract/
_SUBPROJECT_ROOT = _HERE.parents[1]              # dabs-data-product-template/
_SCHEMA_PATH = _SUBPROJECT_ROOT / "data-contract.schema.json"


class ContractError(ValueError):
    """Raised when a data-contract.yml fails validation."""


def _load_schema() -> dict[str, Any]:
    with _SCHEMA_PATH.open() as fh:
        return json.load(fh)


def load(path: str | Path) -> dict[str, Any]:
    """Parse, validate, and return the contract dict.

    Raises:
        ContractError: contract is malformed or violates the JSON Schema.
    """
    p = Path(path)
    if not p.exists():
        raise ContractError(f"Contract file not found: {p}")

    try:
        with p.open() as fh:
            contract: dict[str, Any] = yaml.safe_load(fh) or {}
    except yaml.YAMLError as exc:
        raise ContractError(f"YAML parse error in {p}: {exc}") from exc

    schema = _load_schema()
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(contract), key=lambda e: e.path)
    if errors:
        message_lines = [f"Contract {p} failed schema validation:"]
        for err in errors:
            location = ".".join(str(part) for part in err.absolute_path) or "<root>"
            message_lines.append(f"  - at {location}: {err.message}")
        raise ContractError("\n".join(message_lines))

    return contract


def list_pii_columns(contract: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the subset of schema.columns where pii=True."""
    cols = contract.get("schema", {}).get("columns", [])
    return [c for c in cols if c.get("pii") is True]


def list_quality_expectations(contract: dict[str, Any]) -> list[dict[str, Any]]:
    return list(contract.get("quality_expectations", []))


def list_scoped_views(contract: dict[str, Any]) -> list[dict[str, Any]]:
    return list(contract.get("ai_consumption", {}).get("scoped_views", []))


def list_uc_functions(contract: dict[str, Any]) -> list[dict[str, Any]]:
    return list(contract.get("ai_consumption", {}).get("uc_functions", []))
