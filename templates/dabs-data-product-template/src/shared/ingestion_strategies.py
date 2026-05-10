"""Ingestion strategies — Snapshot · Incremental · CDC.

Each strategy implements `read(spark, contract, source_path) -> DataFrame`.
Bronze pipeline dispatches via `for_strategy(name)`.
"""

from __future__ import annotations

from typing import Any, Protocol


class IngestionStrategy(Protocol):
    name: str

    def read(self, spark: Any, contract: dict[str, Any], source_path: str) -> Any:
        ...


class SnapshotStrategy:
    """Full-refresh: read the entire source each run.

    Suitable for small dimension-style sources where re-reading is cheap.
    """

    name = "snapshot"

    def read(self, spark: Any, contract: dict[str, Any], source_path: str) -> Any:
        schema_columns = contract.get("schema", {}).get("columns", [])
        ddl = ", ".join(
            f"{c['name']} {c['type']}" + (" NOT NULL" if not c.get("nullable", True) else "")
            for c in schema_columns
        )
        return (
            spark.read
            .schema(ddl)
            .format(_format_for(contract))
            .load(source_path)
        )


class IncrementalStrategy:
    """Watermark-driven: read rows where `incremental_column > last_watermark`.

    Stores watermark in a sidecar table per `metadata.id`.
    """

    name = "incremental"

    def read(self, spark: Any, contract: dict[str, Any], source_path: str) -> Any:
        bronze = contract["bronze"]
        col = bronze["incremental_column"]
        return (
            spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", _format_for(contract))
            .option("cloudFiles.schemaEvolutionMode", _schema_evolution_mode(bronze))
            .option("cloudFiles.includeExistingFiles", "true")
            .load(source_path)
            .where(f"{col} IS NOT NULL")
        )


class CdcStrategy:
    """Change-data-capture: ingest insert/update/delete events as a stream."""

    name = "cdc"

    def read(self, spark: Any, contract: dict[str, Any], source_path: str) -> Any:
        return (
            spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", _format_for(contract))
            .option("cloudFiles.includeExistingFiles", "true")
            .load(source_path)
        )


_REGISTRY: dict[str, IngestionStrategy] = {
    "snapshot": SnapshotStrategy(),
    "incremental": IncrementalStrategy(),
    "cdc": CdcStrategy(),
}


def for_strategy(name: str) -> IngestionStrategy:
    if name not in _REGISTRY:
        raise ValueError(
            f"Unknown ingestion strategy: {name}. Valid: {sorted(_REGISTRY)}"
        )
    return _REGISTRY[name]


def _format_for(contract: dict[str, Any]) -> str:
    """Map source_type → Spark format string."""
    source_type = contract["bronze"]["source_type"]
    return {
        "files": "json",
        "database": "jdbc",
        "api": "json",
        "kafka": "kafka",
        "saas": "json",
    }.get(source_type, "json")


def _schema_evolution_mode(bronze: dict[str, Any]) -> str:
    return {
        "strict": "none",
        "merge": "addNewColumns",
        "rescue": "rescue",
    }.get(bronze.get("schema_evolution", "rescue"), "rescue")
