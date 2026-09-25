"""Small grid search over linear GD hyperparameters."""
from __future__ import annotations
import itertools
import numpy as np
from datamind.models.baselines import LinearRegressionGD
from datamind.models.metrics import rmse

def grid_search_linear_gd(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_val: np.ndarray,
    y_val: np.ndarray,
    lrs: list[float] | None = None,
    l2s: list[float] | None = None,
    n_iter: int = 200,
) -> dict:
    lrs = lrs or [0.01, 0.05]
    l2s = l2s or [0.0, 0.1]
    best = {"rmse": float("inf"), "lr": None, "l2": None, "model": None}
    for lr, l2 in itertools.product(lrs, l2s):
        model = LinearRegressionGD(lr=lr, n_iter=n_iter, l2=l2).fit(x_train, y_train)
        score = rmse(y_val, model.predict(x_val))
        if score < best["rmse"]:
            best = {"rmse": score, "lr": lr, "l2": l2, "model": model}
    return best
