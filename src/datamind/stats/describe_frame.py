from __future__ import annotations
import pandas as pd

def describe_numeric(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include='number')
