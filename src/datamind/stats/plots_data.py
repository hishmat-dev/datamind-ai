"""Prepare series for visualization without plotting backends."""
from __future__ import annotations
import numpy as np
import pandas as pd

def histogram_bins(series: pd.Series, bins: int = 10) -> tuple[np.ndarray, np.ndarray]:
    counts, edges = np.histogram(series.dropna().to_numpy(), bins=bins)
    return counts, edges

def top_correlations(corr: pd.DataFrame, column: str, k: int = 5) -> list[tuple[str, float]]:
    if column not in corr.columns:
        return []
    s = corr[column].drop(labels=[column], errors="ignore").abs().sort_values(ascending=False)
    return [(str(idx), float(corr.loc[idx, column])) for idx in s.head(k).index]
