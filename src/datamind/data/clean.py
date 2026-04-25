"""Cleaning and preprocessing utilities."""
from __future__ import annotations
import numpy as np
import pandas as pd


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)


def impute_numeric_median(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    out = df.copy()
    cols = columns or list(out.select_dtypes(include=[np.number]).columns)
    for c in cols:
        if out[c].isna().any():
            out[c] = out[c].fillna(out[c].median())
    return out


def clip_outliers_iqr(df: pd.DataFrame, column: str, factor: float = 1.5) -> pd.DataFrame:
    out = df.copy()
    q1, q3 = out[column].quantile(0.25), out[column].quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    out[column] = out[column].clip(lower=low, upper=high)
    return out


def standardize(df: pd.DataFrame, columns: list[str]) -> tuple[pd.DataFrame, dict[str, tuple[float, float]]]:
    out = df.copy()
    stats: dict[str, tuple[float, float]] = {}
    for c in columns:
        mu = float(out[c].mean())
        sigma = float(out[c].std(ddof=0)) or 1.0
        out[c] = (out[c] - mu) / sigma
        stats[c] = (mu, sigma)
    return out, stats
