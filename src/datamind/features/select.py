"""Simple feature selection by variance and correlation."""
from __future__ import annotations
import numpy as np
import pandas as pd

def high_variance_columns(df: pd.DataFrame, threshold: float = 1e-6) -> list[str]:
    out = []
    for c in df.select_dtypes(include=[np.number]).columns:
        if float(df[c].var(ddof=0)) > threshold:
            out.append(str(c))
    return out

def drop_highly_correlated(df: pd.DataFrame, threshold: float = 0.98) -> list[str]:
    corr = df.select_dtypes(include=[np.number]).corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    return [str(c) for c in upper.columns if any(upper[c] > threshold)]
