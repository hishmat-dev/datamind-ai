
import pandas as pd
from datamind.data.clean import drop_duplicates, impute_numeric_median, standardize
from datamind.data.generate import generate_housing

def test_impute_and_dedupe():
    df = generate_housing(80, seed=3)
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    cleaned = drop_duplicates(df)
    assert len(cleaned) < len(df)
    imputed = impute_numeric_median(cleaned)
    assert imputed["age_years"].isna().sum() == 0

def test_standardize():
    df = generate_housing(40, seed=4)
    out, stats = standardize(df, ["area_sqm"])
    assert abs(out["area_sqm"].mean()) < 1e-6
    assert "area_sqm" in stats
