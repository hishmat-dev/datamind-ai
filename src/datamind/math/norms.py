from __future__ import annotations
import numpy as np

def l2_norm(v: np.ndarray) -> float:
    return float(np.linalg.norm(v))

def l1_norm(v: np.ndarray) -> float:
    return float(np.sum(np.abs(v)))
