"""Pairwise interaction features."""
from __future__ import annotations
import pandas as pd

def add_interaction(df: pd.DataFrame, a: str, b: str, name: str | None = None) -> pd.DataFrame:
    out = df.copy()
    col = name or f"{a}_x_{b}"
    out[col] = out[a] * out[b]
    return out
