"""Train/test splitting with a fixed seed."""
from __future__ import annotations
import numpy as np
import pandas as pd


def train_test_split(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    rng = np.random.default_rng(seed)
    idx = np.arange(len(df))
    rng.shuffle(idx)
    n_test = int(len(df) * test_size)
    test_idx, train_idx = idx[:n_test], idx[n_test:]
    features = [c for c in df.columns if c != target]
    x = df[features]
    y = df[target]
    return (
        x.iloc[train_idx].reset_index(drop=True),
        x.iloc[test_idx].reset_index(drop=True),
        y.iloc[train_idx].reset_index(drop=True),
        y.iloc[test_idx].reset_index(drop=True),
    )
