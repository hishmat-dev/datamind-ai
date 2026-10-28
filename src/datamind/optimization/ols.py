"""Closed-form ordinary least squares vs batch gradient descent lab."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class OLSResult:
    weights: np.ndarray
    bias: float


def closed_form_ols(x: np.ndarray, y: np.ndarray) -> OLSResult:
    x_mean, y_mean = x.mean(0), float(y.mean())
    xc, yc = x - x_mean, y - y_mean
    # pseudo-inverse for stability
    w = np.linalg.pinv(xc) @ yc
    b = y_mean - float(x_mean @ w)
    return OLSResult(weights=w, bias=b)


def batch_gd_ols(
    x: np.ndarray, y: np.ndarray, lr: float = 0.05, n_iter: int = 500
) -> tuple[OLSResult, list[float]]:
    n, d = x.shape
    w, b = np.zeros(d), 0.0
    history: list[float] = []
    for _ in range(n_iter):
        pred = x @ w + b
        err = pred - y
        history.append(float(np.mean(err ** 2)))
        w -= lr * (2 / n) * (x.T @ err)
        b -= lr * float((2 / n) * np.sum(err))
    return OLSResult(weights=w, bias=b), history


def compare_ols_to_gd(
    x: np.ndarray, y: np.ndarray, lr: float = 0.05, n_iter: int = 800
) -> dict[str, float]:
    ols = closed_form_ols(x, y)
    gd, history = batch_gd_ols(x, y, lr=lr, n_iter=n_iter)
    pred_ols = x @ ols.weights + ols.bias
    pred_gd = x @ gd.weights + gd.bias
    return {
        "mse_ols": float(np.mean((pred_ols - y) ** 2)),
        "mse_gd": float(np.mean((pred_gd - y) ** 2)),
        "weight_l2_diff": float(np.linalg.norm(ols.weights - gd.weights)),
        "final_gd_loss": history[-1] if history else float("nan"),
    }
