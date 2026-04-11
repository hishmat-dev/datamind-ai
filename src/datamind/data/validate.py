"""Validate dataframes against schema contracts."""
from __future__ import annotations
import pandas as pd
from datamind.data.schema import DatasetSchema, HOUSING_SCHEMA


class ValidationError(Exception):
    pass


def validate_dataframe(df: pd.DataFrame, schema: DatasetSchema = HOUSING_SCHEMA) -> list[str]:
    """Return list of validation issues (empty if valid)."""
    issues: list[str] = []
    expected = set(schema.column_names())
    actual = set(df.columns)
    missing = expected - actual
    if missing:
        issues.append(f"missing columns: {sorted(missing)}")
    extra = actual - expected
    if extra:
        issues.append(f"unexpected columns: {sorted(extra)}")
    for col in schema.columns:
        if col.name not in df.columns:
            continue
        series = df[col.name]
        if not col.nullable and series.isna().any():
            issues.append(f"nulls in non-nullable column {col.name}")
        if col.dtype == "float" and not pd.api.types.is_numeric_dtype(series):
            issues.append(f"column {col.name} expected numeric")
    return issues


def assert_valid(df: pd.DataFrame, schema: DatasetSchema = HOUSING_SCHEMA) -> None:
    issues = validate_dataframe(df, schema)
    if issues:
        raise ValidationError("; ".join(issues))
