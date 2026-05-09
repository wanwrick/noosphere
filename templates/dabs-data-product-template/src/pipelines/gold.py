"""Gold layer — first cross-source joins + derived/calculated fields.

Per the No LAC principle: **custom code lives only at Gold**. Bronze and
Silver are reusable patterns parameterized by metadata; the first place a
domain expresses opinion is the first cross-source join.

This is the only pipeline file that legitimately contains domain-specific
logic. Forks should fill in the Gold transformations that compose multiple
Silver tables into business-ready facts and dimensions.
"""

from __future__ import annotations

import os
from pathlib import Path

from src.contract import load

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
    if dlt is None:                                 # pragma: no cover
        raise NotImplementedError(
            "gold.py is a DLT notebook; run inside Databricks for the full pipeline."
        )

    table_name = f"{contract['metadata']['id']}_gold"
    silver_table = f"{contract['metadata']['id']}_silver"

    @dlt.table(name=table_name, comment="Gold — cross-source joins + derived fields.")   # type: ignore[misc]
    def gold_table():
        df = dlt.read(silver_table)                                                       # type: ignore[attr-defined]
        # ----------------------------------------------------------------
        # CUSTOM CODE LIVES HERE. This is the only Medallion layer where
        # domain-specific opinion is allowed. Fill in cross-source joins
        # and derived calculations per your business logic.
        # ----------------------------------------------------------------
        return df


if __name__ == "__main__" and dlt is not None:      # pragma: no cover
    main()
