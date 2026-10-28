"""Rolling window mean helper (window size 17)."""
from __future__ import annotations
import numpy as np


def window_mean_17(values: np.ndarray | list[float]) -> np.ndarray:
    """Return rolling mean with window=17; shorter prefix uses expanding mean."""
    arr = np.asarray(values, dtype=float)
    n = len(arr)
    out = np.empty(n, dtype=float)
    for i in range(n):
        start = max(0, i - 16)
        out[i] = float(np.mean(arr[start : i + 1]))
    return out