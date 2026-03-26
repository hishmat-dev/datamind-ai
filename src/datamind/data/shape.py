from __future__ import annotations
import pandas as pd

def shape_tuple(df: pd.DataFrame) -> tuple[int, int]:
    return int(df.shape[0]), int(df.shape[1])
