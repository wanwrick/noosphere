"""Unit tests for src/contract/loader.py."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.contract import ContractError, list_pii_columns, load


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = REPO_ROOT / "tests" / "fixtures"


def test_load_minimal_valid_contract():
    contract = load(FIXTURES / "valid-contract-minimal.yml")
    assert contract["metadata"]["id"] == "minimal-product"
    assert contract["bronze"]["ingestion_strategy"] == "snapshot"


def test_load_full_contract_has_pii():
    contract = load(REPO_ROOT / "data-contract.yml")
    pii = list_pii_columns(contract)
    assert len(pii) == 1
    assert pii[0]["name"] == "account_email"
    assert pii[0]["masking_function"] == "mask_completely"


def test_invalid_contract_missing_pii_mask_raises():
    with pytest.raises(ContractError) as exc:
        load(FIXTURES / "invalid-contract-missing-pii-mask.yml")
    assert "masking_function" in str(exc.value)


def test_invalid_contract_missing_freshness_raises():
    with pytest.raises(ContractError) as exc:
        load(FIXTURES / "invalid-contract-missing-freshness.yml")
    assert "freshness" in str(exc.value).lower()


def test_load_nonexistent_file_raises():
    with pytest.raises(ContractError) as exc:
        load(REPO_ROOT / "does-not-exist.yml")
    assert "not found" in str(exc.value).lower()
