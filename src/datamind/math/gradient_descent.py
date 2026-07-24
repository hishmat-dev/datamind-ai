"""Educational gradient-descent utilities with analytical checks."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class GDResult:
    params: np.ndarray
    history: list[float]
    n_iter: int


def quadratic_loss(theta: np.ndarray, a: float = 1.0, b: float = 0.0) -> float:
    """f(theta) = a * ||theta||^2 + b."""
    return float(a * np.sum(theta ** 2) + b)


def quadratic_grad(theta: np.ndarray, a: float = 1.0) -> np.ndarray:
    return 2.0 * a * theta


def gradient_descent(
    theta0: np.ndarray,
    grad_fn,
    loss_fn,
    lr: float = 0.1,
    n_iter: int = 100,
    tol: float = 1e-8,
) -> GDResult:
    theta = theta0.astype(float).copy()
    history: list[float] = []
    for i in range(n_iter):
        g = grad_fn(theta)
        theta = theta - lr * g
        loss = float(loss_fn(theta))
        history.append(loss)
        if np.linalg.norm(g) < tol:
            return GDResult(theta, history, i + 1)
    return GDResult(theta, history, n_iter)


def numerical_gradient(f, theta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    grad = np.zeros_like(theta, dtype=float)
    for i in range(len(theta)):
        e = np.zeros_like(theta)
        e[i] = eps
        grad[i] = (f(theta + e) - f(theta - e)) / (2 * eps)
    return grad
