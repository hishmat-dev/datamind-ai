"""Model-agnostic and linear feature importance."""
from __future__ import annotations
import numpy as np
from datamind.models.metrics import mse


def linear_coefficient_importance(weights: np.ndarray, feature_names: list[str]) -> dict[str, float]:
    abs_w = np.abs(weights)
    total = float(np.sum(abs_w)) or 1.0
    return {name: float(v / total) for name, v in zip(feature_names, abs_w, strict=True)}


def permutation_importance(
    predict_fn,
    x: np.ndarray,
    y: np.ndarray,
    feature_names: list[str],
    seed: int = 42,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    baseline = mse(y, predict_fn(x))
    importances: dict[str, float] = {}
    for i, name in enumerate(feature_names):
        x_perm = x.copy()
        rng.shuffle(x_perm[:, i])
        perm_score = mse(y, predict_fn(x_perm))
        importances[name] = float(perm_score - baseline)
    return importances
