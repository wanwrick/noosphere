"""Bronze layer — raw landing, append-only, audit-grade.

Reads `data-contract.yml` and dispatches to one of three ingestion strategies
based on `bronze.ingestion_strategy`:

    - snapshot     -> full-refresh from source each run
    - incremental  -> watermark-driven via `incremental_column`
    - cdc          -> change-data-capture (Auto Loader / Lakeflow Connect)

This file is loaded as a DLT notebook by the bundle. The Databricks runtime
provides `dlt`; locally the helpers raise NotImplementedError so unit tests
can import the contract logic without a Databricks runtime.
"""

from __future__ import annotations

import os
from pathlib import Path

from src.contract import load
from src.shared.ingestion_strategies import for_strategy

try:
    import dlt   # type: ignore[import]
except ImportError:                                # pragma: no cover
    dlt = None   # local import shim


def _resolve_contract_path() -> Path:
    """DLT passes runtime config; locally we fall back to repo root."""
    if dlt is not None:
        cfg_path = (
            spark.conf.get("contract_path", "data-contract.yml")  # type: ignore[name-defined]
        )
    else:
        cfg_path = os.environ.get("CONTRACT_PATH", "data-contract.yml")
    return Path(cfg_path)


def main() -> None:
    contract = load(_resolve_contract_path())
    strategy = for_strategy(contract["bronze"]["ingestion_strategy"])

    if dlt is None:                                 # pragma: no cover
        raise NotImplementedError(
            "bronze.py is a DLT notebook; run inside Databricks for the full pipeline."
        )

    table_name = f"{contract['metadata']['id']}_bronze"
    raw_path = contract.get("bronze", {}).get("source_path", "<configure-per-target>")

    @dlt.table(                                     # type: ignore[misc]
        name=table_name,
        comment=f"Bronze layer for {contract['metadata']['name']} — raw landing.",
    )
    def bronze_table():
        return strategy.read(spark, contract, raw_path)   # type: ignore[name-defined]


if __name__ == "__main__" and dlt is not None:      # pragma: no cover
    main()
