"""Platinum layer — semantic + AI-ready scoped views + UC Functions.

Reads `data-contract.yml`'s `ai_consumption.scoped_views[]` and registers
each as a DLT view. UC Functions are registered separately by the
governance pipeline (`src/shared/unity_catalog_helpers.py`).
"""

from __future__ import annotations

import os
from pathlib import Path

from src.contract import load, list_scoped_views

try:
    import dlt   # type: ignore[import]
except ImportError:                                # pragma: no cover
    dlt = None


def _resolve_contract_path() -> Path:
    if dlt is not None:
        cfg_path = spark.conf.get("contract_path", "data-contract.yml")  # type: ignore[name-defined]
    else:
        cfg_path = os.environ.get("CONTRACT_PATH", "data-contract.yml")
    return Path(cfg_path)


def main() -> None:
    contract = load(_resolve_contract_path())
    views = list_scoped_views(contract)
    if not contract.get("ai_consumption", {}).get("enabled", False):
        return                                        # nothing to do

    if dlt is None:                                 # pragma: no cover
        raise NotImplementedError(
            "platinum.py is a DLT notebook; run inside Databricks for the full pipeline."
        )

    gold_table = f"{contract['metadata']['id']}_gold"

    for view in views:
        view_name = view["name"]
        cols = view.get("columns", [])
        select_clause = ", ".join(cols) if cols else "*"

        # Use a closure factory so each DLT view gets its own function.
        def _make_view(name: str, cols_str: str):
            @dlt.table(                                                       # type: ignore[misc]
                name=name,
                comment=view.get("description", "AI-ready scoped view."),
            )
            def _view():
                return spark.sql(f"SELECT {cols_str} FROM LIVE.{gold_table}")  # type: ignore[name-defined]
            return _view

        _make_view(view_name, select_clause)


if __name__ == "__main__" and dlt is not None:      # pragma: no cover
    main()
