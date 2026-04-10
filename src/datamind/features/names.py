from __future__ import annotations
import pandas as pd
import numpy as np

def numeric_columns(df: pd.DataFrame) -> list[str]:
    return [str(c) for c in df.select_dtypes(include=[np.number]).columns]
