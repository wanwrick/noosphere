# Testing Patterns - DataWizards Stack

> Test frameworks, standard scenarios, mock strategies, and coverage targets for the DataWizards data engineering stack (PySpark, DLT, SQL migration, APIs).

## Framework Selection

| Context | Framework | Why |
|---------|-----------|-----|
| Python / PySpark transformation | pytest + chispa | DataFrame assertions, fixtures |
| SQL / DBT model | dbt test + dbt-expectations | Native SQL testing |
| API / connections | pytest + responses / moto | Mock external services |
| Integration / E2E | testcontainers | Spin up real databases |
| GCP service mocking | moto | Pub/Sub, GCS, BigQuery |
| Coverage reporting | coverage.py | `pytest --cov=src --cov-report=html` |

---

## Standard Test Scenarios by Context

### Data Transformation (PySpark / Spark SQL)

Always include these in the Outcome section:
```
- Happy path: valid input produces expected output
- Empty DataFrame: returns empty output, no crash
- NULL values in key columns: handled per business rule (drop / coalesce / fail)
- Duplicate records: dedup logic removes correct rows
- Invalid data types: string in numeric column raises appropriate error
- Boundary values: min/max dates, zero, negative numbers
- Schema changes: missing column, extra column - handled gracefully
- Late-arriving records: incremental logic handles out-of-order data
```

**Example structure - PySpark with chispa:**
```python
import pytest
from chispa import assert_df_equality
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("test").getOrCreate()

def test_transform_happy_path(spark):
    input_data = [("ARR001", 1000.0, "2024-01-15"), ("ARR002", 500.0, "2024-01-16")]
    expected_data = [("ARR001", 1000.0), ("ARR002", 500.0)]
    input_df = spark.createDataFrame(input_data, ["arrangement_id", "balance", "date"])
    result = transform_balance(input_df)
    expected = spark.createDataFrame(expected_data, ["arrangement_id", "balance"])
    assert_df_equality(result, expected, ignore_row_order=True)

def test_transform_empty_input(spark):
    input_df = spark.createDataFrame([], schema)
    result = transform_balance(input_df)
    assert result.count() == 0

def test_transform_null_key(spark):
    input_data = [(None, 1000.0), ("ARR001", 500.0)]
    input_df = spark.createDataFrame(input_data, ["arrangement_id", "balance"])
    result = transform_balance(input_df)
    # NULL arrangement_id should be dropped
    assert result.filter(result.arrangement_id.isNull()).count() == 0
```

---

### DLT Data Quality Expectations

For every new DLT pipeline, document the 5 baseline expectations in the task:

```python
# In the DLT pipeline, the 5 baseline expectations must be implemented:

import dlt

@dlt.table
@dlt.expect_or_fail("not_null_arrangement_id", "arrangement_id IS NOT NULL")
@dlt.expect_or_fail("unique_key", "arrangement_id IS NOT NULL")  # enforce upstream
@dlt.expect_or_drop("valid_balance_range", "balance BETWEEN -1000000 AND 100000000")
@dlt.expect_or_fail("schema_conformance", "arrangement_id IS NOT NULL AND product_code IS NOT NULL")
def silver_lms_arrangement():
    return (
        dlt.read("bronze_lms_arrangement")
        # transformation logic
    )
```

**Quarantine routing pattern (from Gabriel Goulart / Yelena Hakhumyan):**
```python
# Records dropped by expect_or_drop get routed to quarantine via force_batch_sync
# Consult Gabriel or Yelena for the current quarantine table pattern
# Target: silver_uat.{domain}.quarantine_{table_name}
```

---

### Connection / API Tests

```
- Successful connection with valid credentials
- Authentication failure (wrong/expired credentials) → raises AuthError
- Network timeout → raises TimeoutError after retries
- Retry logic: transient failure then success
- Rate limiting response → handled with backoff
- Invalid endpoint → clear error message
```

**Example - BigQuery / OAuth2 connection:**
```python
from unittest.mock import Mock, patch
import pytest

def test_bq_connection_success():
    with patch('google.cloud.bigquery.Client') as mock_client:
        mock_client.return_value.query.return_value = Mock(result=lambda: [])
        result = connect_to_bq(project="qt-mortgages-prod-3r", credentials=valid_creds)
        assert result is not None

def test_bq_connection_auth_failure():
    with patch('google.cloud.bigquery.Client') as mock_client:
        mock_client.side_effect = Exception("Invalid credentials")
        with pytest.raises(Exception, match="Invalid credentials"):
            connect_to_bq(project="qt-mortgages-prod-3r", credentials=bad_creds)
```

---

### Array Explosion Tests

For the inline_outer / from_json pattern:

```
- Array with multiple elements: all elements exploded to separate rows
- Array with single element: one row returned
- NULL array value: row preserved with NULL exploded columns (outer semantics)
- Empty array []: row preserved with NULL exploded columns (outer semantics)
- Malformed JSON string: handled gracefully (quarantine or NULL)
- Nested struct within array: correct field extraction
```

```python
def test_explode_null_array(spark):
    """NULL array preserves parent row with NULL child columns (outer semantics)"""
    input_data = [("LOAN001", None), ("LOAN002", '[{"borrowerId":"B1","type":1}]')]
    df = spark.createDataFrame(input_data, ["loan_id", "borrowers_json"])
    result = explode_borrowers(df)
    # LOAN001 should still appear with NULL borrower fields
    loan001 = result.filter(result.loan_id == "LOAN001")
    assert loan001.count() == 1
    assert loan001.first().borrower_id is None

def test_explode_multiple_borrowers(spark):
    """Multiple borrowers in array → multiple rows"""
    borrowers = '[{"borrowerId":"B1","type":1},{"borrowerId":"B2","type":2}]'
    input_data = [("LOAN001", borrowers)]
    df = spark.createDataFrame(input_data, ["loan_id", "borrowers_json"])
    result = explode_borrowers(df)
    assert result.filter(result.loan_id == "LOAN001").count() == 2
```

---

### SQL Migration Validation Tests

When validating a SQL Server → Databricks SQL migration:

```
- Row count: Databricks output == SQL Server output for same date range
- Checksum: sum of key numeric columns matches
- Sample record comparison: spot-check 20-50 records for field-by-field match
- NULL handling: ISNULL() → COALESCE() produces same results on NULLable columns
- Date functions: GETDATE() equivalent produces same dates (timezone-aware)
- CROSS APPLY replacement: lateral view produces identical row expansion
```

---

## Mock Data Strategies

### PySpark DataFrame Mocks

```python
# Factory for consistent test DataFrames
def create_test_lms_arrangement(spark, data=None):
    default_data = [
        ("ARR001", "MORTGAGE", 250000.0, "2024-01-01", "ACTIVE"),
        ("ARR002", "RENEWAL", 180000.0, "2024-01-15", "PENDING"),
    ]
    schema = "arrangement_id STRING, product_type STRING, balance DOUBLE, effective_date STRING, status STRING"
    return spark.createDataFrame(data or default_data, schema)

# Standard boundary data sets
EMPTY_DF_DATA = []
NULL_KEY_DATA = [(None, "MORTGAGE", 100.0), ("ARR001", "RENEWAL", 200.0)]
DUPLICATE_DATA = [("ARR001", "MORTGAGE", 100.0), ("ARR001", "MORTGAGE", 100.0)]
```

### External Service Mocks

```python
# Mock GCP Pub/Sub
@patch('google.cloud.pubsub_v1.SubscriberClient')
def test_ingest_lms_messages(mock_client):
    mock_client.return_value.pull.return_value = mock_pubsub_response
    result = ingest_from_pubsub(subscription="lms-subscription")
    assert result.count() == expected_message_count

# Mock Databricks secrets (for Airflow/secrets usage)
@patch('databricks.sdk.WorkspaceClient')
def test_read_secret(mock_ws):
    mock_ws.return_value.secrets.get.return_value = Mock(value="test_value")
    result = get_secret("equifax-api-key")
    assert result == "test_value"
```

---

## Coverage Requirements

| Component | Minimum | Critical Paths |
|-----------|---------|----------------|
| Core transformation logic | >80% | 100% |
| Business rules (dedup, balance calc) | >80% | 100% |
| DLT quality expectation logic | >80% | 100% |
| Error handling | >70% | 100% for critical errors |
| Utility functions | >70% | N/A |
| Connection / auth logic | >80% | 100% |

### pytest Commands

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=src --cov-report=html tests/

# Run specific domain tests
pytest tests/test_lms_transformations.py
pytest tests/test_temenos_silver.py

# Run with verbose output
pytest -v tests/

# Run only tests matching keyword
pytest -k "test_balance or test_arrangement"
```
