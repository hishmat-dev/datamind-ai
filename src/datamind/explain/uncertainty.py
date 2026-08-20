"""Simple uncertainty estimates via residual std and bootstrap."""
from __future__ import annotations
import numpy as np


def residual_std(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.std(y_true - y_pred, ddof=1)) if len(y_true) > 1 else 0.0


def prediction_interval(
    y_pred: np.ndarray, residual_sigma: float, z: float = 1.96
) -> tuple[np.ndarray, np.ndarray]:
    low = y_pred - z * residual_sigma
    high = y_pred + z * residual_sigma
    return low, high


def bootstrap_metric(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    metric_fn,
    n_boot: int = 200,
    seed: int = 42,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        scores.append(float(metric_fn(y_true[idx], y_pred[idx])))
    arr = np.asarray(scores, dtype=float)
    return {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr, ddof=1)),
        "p05": float(np.percentile(arr, 5)),
        "p95": float(np.percentile(arr, 95)),
    }
