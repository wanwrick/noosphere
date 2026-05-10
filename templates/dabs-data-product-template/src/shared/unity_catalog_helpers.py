"""Unity Catalog helpers — apply tags, masking functions, grants from contract.

Pure-Python helpers that emit the SQL Databricks needs to enforce contract
metadata at the UC level. Designed to be called from the bundle deploy hook
or directly from a notebook task.
"""

from __future__ import annotations

from typing import Any


def emit_column_tag_statements(
    contract: dict[str, Any],
    catalog: str,
    schema_layer: str = "silver",
) -> list[str]:
    """ALTER TABLE statements to set column tags from contract.

    Tags applied:
        - classification = <public|internal|confidential|restricted>
        - pii = <true|false>
        - owner_team = <metadata.owner_team>
    """
    table = f"{catalog}.{contract['metadata']['id']}.{contract['metadata']['id']}_{schema_layer}"
    owner = contract["metadata"]["owner_team"]
    statements: list[str] = []
    for col in contract.get("schema", {}).get("columns", []):
        col_name = col["name"]
        classification = col.get("classification", "internal")
        pii = "true" if col.get("pii") else "false"
        statements.append(
            f"ALTER TABLE {table} ALTER COLUMN {col_name} "
            f"SET TAGS ('classification' = '{classification}', "
            f"'pii' = '{pii}', "
            f"'owner_team' = '{owner}')"
        )
    return statements


def emit_masking_function_statements(
    contract: dict[str, Any],
    catalog: str,
    schema_layer: str = "silver",
) -> list[str]:
    """ALTER COLUMN ... SET MASK statements for every PII column."""
    table = f"{catalog}.{contract['metadata']['id']}.{contract['metadata']['id']}_{schema_layer}"
    statements: list[str] = []
    for col in contract.get("schema", {}).get("columns", []):
        if not col.get("pii"):
            continue
        masking = col.get("masking_function")
        if not masking:                      # contract validation should prevent this
            continue
        statements.append(
            f"ALTER TABLE {table} ALTER COLUMN {col['name']} SET MASK {catalog}.governance.{masking}"
        )
    return statements


def emit_uc_function_statements(contract: dict[str, Any], catalog: str) -> list[str]:
    """CREATE FUNCTION statements for every UC Function declared in the contract.

    Returns *placeholder* statements — operators fill in the function body
    before deployment. The skeleton ensures registration is governed.
    """
    fns = contract.get("ai_consumption", {}).get("uc_functions", [])
    statements: list[str] = []
    for fn in fns:
        name = fn["name"]
        statements.append(
            f"-- Governed by: {fn.get('governance', 'producer-owned')}\n"
            f"-- Logic summary: {fn.get('logic_summary', '<none>')}\n"
            f"CREATE OR REPLACE FUNCTION {catalog}.functions.{name}(...) "
            f"RETURNS <type> RETURN <expr>;"
        )
    return statements


def emit_grant_statements(
    contract: dict[str, Any],
    catalog: str,
    consumer_group: str = "data_consumers_internal",
) -> list[str]:
    """GRANT statements honoring metadata.classification."""
    schema_fqn = f"{catalog}.{contract['metadata']['id']}"
    classification = contract["metadata"]["classification"]
    statements: list[str] = [
        f"GRANT USE SCHEMA ON SCHEMA {schema_fqn} TO `{consumer_group}`",
        f"GRANT SELECT ON SCHEMA {schema_fqn} TO `{consumer_group}`",
    ]
    if classification == "restricted":
        # Restricted classification overrides default consumer access; require
        # an explicit cleared group.
        statements.append(
            f"REVOKE ALL PRIVILEGES ON SCHEMA {schema_fqn} FROM `{consumer_group}`"
        )
    return statements
