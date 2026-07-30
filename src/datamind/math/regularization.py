"""Regularization penalties and closed-form ridge regression."""
from __future__ import annotations
import numpy as np


def l2_penalty(weights: np.ndarray, alpha: float) -> float:
    return float(alpha * np.sum(weights ** 2))


def l1_penalty(weights: np.ndarray, alpha: float) -> float:
    return float(alpha * np.sum(np.abs(weights)))


def ridge_closed_form(x: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """Solve (X^T X + alpha I) w = X^T y with intercept excluded from X."""
    d = x.shape[1]
    xtx = x.T @ x + alpha * np.eye(d)
    xty = x.T @ y
    return np.linalg.solve(xtx, xty)
