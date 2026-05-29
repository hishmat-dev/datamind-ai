"""Feature engineering transforms."""
from __future__ import annotations
import numpy as np
import pandas as pd


def add_area_per_room(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    rooms = out["rooms"].replace(0, np.nan)
    out["area_per_room"] = out["area_sqm"] / rooms
    out["area_per_room"] = out["area_per_room"].fillna(out["area_sqm"])
    return out


def add_age_band(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["age_band"] = pd.cut(
        out["age_years"].fillna(out["age_years"].median()),
        bins=[-0.1, 5, 15, 30, 100],
        labels=["new", "mid", "old", "historic"],
    ).astype(str)
    return out


def add_log_price(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["log_price"] = np.log1p(out["price"])
    return out


def polynomial_features(df: pd.DataFrame, columns: list[str], degree: int = 2) -> pd.DataFrame:
    out = df.copy()
    if degree < 2:
        return out
    for c in columns:
        out[f"{c}_sq"] = out[c] ** 2
    return out
