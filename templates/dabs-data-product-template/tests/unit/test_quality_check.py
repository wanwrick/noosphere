"""Unit tests for src/contract/quality_check.py."""

from __future__ import annotations

from src.contract.quality_check import run_quality_check, to_dlt_decorator_name


def test_run_quality_check_clean():
    expectations = [
        {"name": "pk_not_null", "expectation": "id IS NOT NULL", "on_violation": "fail"},
        {"name": "amount_pos", "expectation": "amount > 0", "on_violation": "drop"},
    ]
    result = run_quality_check(expectations)
    assert result.is_clean
    assert len(result.specs) == 2


def test_run_quality_check_invalid_violation():
    expectations = [
        {"name": "x", "expectation": "x IS NOT NULL", "on_violation": "explode"},
    ]
    result = run_quality_check(expectations)
    assert not result.is_clean
    assert any("explode" in e for e in result.errors)


def test_run_quality_check_missing_fields():
    expectations = [{"name": "x"}]   # missing expectation + on_violation
    result = run_quality_check(expectations)
    assert not result.is_clean


def test_dlt_decorator_mapping():
    assert to_dlt_decorator_name("fail") == "expect_or_fail"
    assert to_dlt_decorator_name("drop") == "expect_or_drop"
    assert to_dlt_decorator_name("drop_to_quarantine") == "expect_or_drop"
    assert to_dlt_decorator_name("warn") == "expect"
