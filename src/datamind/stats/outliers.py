"""Outlier detection helpers."""
from __future__ import annotations
import numpy as np
import pandas as pd


def iqr_outlier_mask(series: pd.Series, factor: float = 1.5) -> pd.Series:
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    return (series < low) | (series > high)


def zscore_outlier_mask(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    mu = series.mean()
    sigma = series.std(ddof=0) or 1.0
    z = (series - mu) / sigma
    return z.abs() > threshold


def outlier_report(df: pd.DataFrame, column: str) -> dict[str, int]:
    s = df[column]
    return {
        "iqr_outliers": int(iqr_outlier_mask(s).sum()),
        "zscore_outliers": int(zscore_outlier_mask(s).sum()),
        "n": int(len(s)),
    }
