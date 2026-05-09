"""Silver layer — clean + standardize + apply DLT expectations from contract.

Reads `data-contract.yml`'s `quality_expectations[]`, compiles them via
src/contract/quality_check.py, and emits the appropriate DLT decorator
(`@dlt.expect`, `@dlt.expect_or_drop`, `@dlt.expect_or_fail`) per
expectation.
"""

from __future__ import annotations

import os
from pathlib import Path

from src.contract import load, run_quality_check
from src.contract.quality_check import to_dlt_decorator_name

try:
    import dlt   # type: ignore[import]
except ImportError:                                # pragma: no cover
    dlt = None


def _resolve_contract_path() -> Path:
    if dlt is not None:
        cfg_path = (
            spark.conf.get("contract_path", "data-contract.yml")  # type: ignore[name-defined]
        )
    else:
        cfg_path = os.environ.get("CONTRACT_PATH", "data-contract.yml")
    return Path(cfg_path)


def main() -> None:
    contract = load(_resolve_contract_path())
    qc = run_quality_check(contract.get("quality_expectations", []))
    if not qc.is_clean:
        raise RuntimeError("Quality expectations malformed:\n" + "\n".join(qc.errors))

    if dlt is None:                                 # pragma: no cover
        raise NotImplementedError(
            "silver.py is a DLT notebook; run inside Databricks for the full pipeline."
        )

    table_name = f"{contract['metadata']['id']}_silver"
    bronze_table = f"{contract['metadata']['id']}_bronze"

    # Build the table function with expectations applied dynamically.
    decorators = []
    for spec in qc.specs:
        decorator = getattr(dlt, to_dlt_decorator_name(spec["on_violation"]))
        decorators.append(decorator(spec["name"], spec["expectation"]))

    @dlt.table(name=table_name, comment="Silver — cleaned + standardized.")   # type: ignore[misc]
    def silver_table():
        df = dlt.read(bronze_table)                                            # type: ignore[attr-defined]
        # Apply per-row casting + standardization as needed; left to extenders.
        return df

    # Apply expectations procedurally (DLT supports decorator chaining).
    for dec in decorators:
        silver_table = dec(silver_table)             # type: ignore[assignment]


if __name__ == "__main__" and dlt is not None:      # pragma: no cover
    main()
