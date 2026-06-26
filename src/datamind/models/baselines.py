"""Simple baseline models implemented without sklearn dependency for core logic."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class MeanBaseline:
    """Predict the training mean for every sample."""
    mean_: float = 0.0

    def fit(self, x: np.ndarray, y: np.ndarray) -> MeanBaseline:
        self.mean_ = float(np.mean(y))
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.full(shape=(len(x),), fill_value=self.mean_, dtype=float)


@dataclass
class LinearRegressionGD:
    """Linear regression trained with batch gradient descent."""
    lr: float = 0.01
    n_iter: int = 1000
    l2: float = 0.0
    weights_: np.ndarray | None = None
    bias_: float = 0.0
    loss_history_: list[float] | None = None

    def fit(self, x: np.ndarray, y: np.ndarray) -> LinearRegressionGD:
        n, d = x.shape
        w = np.zeros(d)
        b = 0.0
        history: list[float] = []
        for _ in range(self.n_iter):
            pred = x @ w + b
            err = pred - y
            loss = float(np.mean(err ** 2) + self.l2 * np.sum(w ** 2))
            history.append(loss)
            grad_w = (2.0 / n) * (x.T @ err) + 2.0 * self.l2 * w
            grad_b = float((2.0 / n) * np.sum(err))
            w = w - self.lr * grad_w
            b = b - self.lr * grad_b
        self.weights_ = w
        self.bias_ = b
        self.loss_history_ = history
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        if self.weights_ is None:
            raise RuntimeError("model not fitted")
        return x @ self.weights_ + self.bias_
