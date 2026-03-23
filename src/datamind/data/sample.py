from __future__ import annotations
import pandas as pd

def head_sample(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return df.head(n).copy()
