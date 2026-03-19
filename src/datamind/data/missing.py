"""Missing-value analysis helpers."""
from __future__ import annotations
import pandas as pd

def missing_report(df: pd.DataFrame) -> dict[str, float]:
    n = len(df) or 1
    return {str(c): float(df[c].isna().mean()) for c in df.columns}

def columns_with_missing(df: pd.DataFrame, threshold: float = 0.0) -> list[str]:
    report = missing_report(df)
    return [c for c, rate in report.items() if rate > threshold]
