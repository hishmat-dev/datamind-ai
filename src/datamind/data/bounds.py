"""Soft bounds checks for housing features."""
from __future__ import annotations
import pandas as pd

BOUNDS = {
    "rooms": (1.0, 12.0),
    "area_sqm": (15.0, 400.0),
    "price": (10_000.0, 5_000_000.0),
}

def out_of_bounds_mask(df: pd.DataFrame, column: str) -> pd.Series:
    low, high = BOUNDS[column]
    return (df[column] < low) | (df[column] > high)

def count_out_of_bounds(df: pd.DataFrame, column: str) -> int:
    return int(out_of_bounds_mask(df, column).sum())
