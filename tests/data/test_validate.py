import pandas as pd
import pytest
from datamind.data.generate import generate_housing
from datamind.data.validate import ValidationError, assert_valid, validate_dataframe

def test_missing_column_detected():
    df = generate_housing(50, seed=1).drop(columns=["rooms"])
    issues = validate_dataframe(df)
    assert any("missing" in i for i in issues)

def test_assert_valid_ok():
    assert_valid(generate_housing(30, seed=2))
