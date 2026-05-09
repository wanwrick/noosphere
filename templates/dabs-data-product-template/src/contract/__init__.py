"""Contract package — loader + checks + AI consumption contract generator.

Public API:
    load(path) -> dict                              # parse + validate
    SchemaCheckResult, run_schema_check(...)        # contract.schema vs actual
    FreshnessCheckResult, run_freshness_check(...)
    QualityCheckResult, run_quality_check(...)
    generate_ai_consumption_contract(contract) -> str
"""

from .loader import (
    ContractError,
    list_pii_columns,
    list_quality_expectations,
    list_scoped_views,
    list_uc_functions,
    load,
)
from .schema_check import SchemaCheckResult, run_schema_check
from .freshness_check import FreshnessCheckResult, run_freshness_check
from .quality_check import QualityCheckResult, run_quality_check
from .ai_contract_generator import generate_ai_consumption_contract

__all__ = [
    "ContractError",
    "load",
    "list_pii_columns",
    "list_quality_expectations",
    "list_scoped_views",
    "list_uc_functions",
    "SchemaCheckResult",
    "run_schema_check",
    "FreshnessCheckResult",
    "run_freshness_check",
    "QualityCheckResult",
    "run_quality_check",
    "generate_ai_consumption_contract",
]
