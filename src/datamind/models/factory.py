"""Model factory: 5 regression + 4 classification estimators (numpy-only)."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np


# ---- Regression ----
@dataclass
class MeanRegressor:
    mean_: float = 0.0
    def fit(self, x: np.ndarray, y: np.ndarray) -> MeanRegressor:
        self.mean_ = float(np.mean(y)); return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.full(len(x), self.mean_)


@dataclass
class LinearGDRegressor:
    lr: float = 0.05
    n_iter: int = 400
    l2: float = 0.0
    weights_: np.ndarray | None = None
    bias_: float = 0.0
    def fit(self, x: np.ndarray, y: np.ndarray) -> LinearGDRegressor:
        n, d = x.shape
        w, b = np.zeros(d), 0.0
        for _ in range(self.n_iter):
            err = x @ w + b - y
            w -= self.lr * ((2 / n) * (x.T @ err) + 2 * self.l2 * w)
            b -= self.lr * float((2 / n) * np.sum(err))
        self.weights_, self.bias_ = w, b
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.weights_ is not None
        return x @ self.weights_ + self.bias_


@dataclass
class RidgeRegressor:
    alpha: float = 1.0
    weights_: np.ndarray | None = None
    bias_: float = 0.0
    def fit(self, x: np.ndarray, y: np.ndarray) -> RidgeRegressor:
        # center for intercept
        x_mean, y_mean = x.mean(0), float(y.mean())
        xc, yc = x - x_mean, y - y_mean
        d = x.shape[1]
        w = np.linalg.solve(xc.T @ xc + self.alpha * np.eye(d), xc.T @ yc)
        self.weights_ = w
        self.bias_ = y_mean - float(x_mean @ w)
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.weights_ is not None
        return x @ self.weights_ + self.bias_


@dataclass
class KNNRegressor:
    k: int = 5
    x_train_: np.ndarray | None = None
    y_train_: np.ndarray | None = None
    def fit(self, x: np.ndarray, y: np.ndarray) -> KNNRegressor:
        self.x_train_, self.y_train_ = x, y
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.x_train_ is not None and self.y_train_ is not None
        preds = []
        for row in x:
            dist = np.linalg.norm(self.x_train_ - row, axis=1)
            idx = np.argsort(dist)[: self.k]
            preds.append(float(np.mean(self.y_train_[idx])))
        return np.asarray(preds)


@dataclass
class MedianRegressor:
    median_: float = 0.0
    def fit(self, x: np.ndarray, y: np.ndarray) -> MedianRegressor:
        self.median_ = float(np.median(y)); return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.full(len(x), self.median_)


# ---- Classification ----
@dataclass
class MajorityClassifier:
    label_: object = 0
    def fit(self, x: np.ndarray, y: np.ndarray) -> MajorityClassifier:
        vals, counts = np.unique(y, return_counts=True)
        self.label_ = vals[int(np.argmax(counts))]
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.full(len(x), self.label_)
    def predict_proba_positive(self, x: np.ndarray) -> np.ndarray:
        return np.full(len(x), 0.5)


@dataclass
class LogisticGDClassifier:
    lr: float = 0.1
    n_iter: int = 500
    l2: float = 0.01
    weights_: np.ndarray | None = None
    bias_: float = 0.0
    classes_: np.ndarray | None = None
    def fit(self, x: np.ndarray, y: np.ndarray) -> LogisticGDClassifier:
        self.classes_ = np.unique(y)
        if len(self.classes_) != 2:
            # one-vs-rest on first two for simplicity when multi-class
            y_bin = (y == self.classes_[0]).astype(float)
        else:
            y_bin = (y == self.classes_[1]).astype(float)
        n, d = x.shape
        w, b = np.zeros(d), 0.0
        for _ in range(self.n_iter):
            z = x @ w + b
            p = 1 / (1 + np.exp(-np.clip(z, -30, 30)))
            err = p - y_bin
            w -= self.lr * ((x.T @ err) / n + self.l2 * w)
            b -= self.lr * float(np.mean(err))
        self.weights_, self.bias_ = w, b
        return self
    def decision_function(self, x: np.ndarray) -> np.ndarray:
        assert self.weights_ is not None
        return x @ self.weights_ + self.bias_
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.classes_ is not None
        scores = self.decision_function(x)
        if len(self.classes_) == 2:
            return np.where(scores >= 0, self.classes_[1], self.classes_[0])
        return np.where(scores >= 0, self.classes_[0], self.classes_[min(1, len(self.classes_)-1)])
    def predict_proba_positive(self, x: np.ndarray) -> np.ndarray:
        z = self.decision_function(x)
        return 1 / (1 + np.exp(-np.clip(z, -30, 30)))


@dataclass
class KNNClassifier:
    k: int = 5
    x_train_: np.ndarray | None = None
    y_train_: np.ndarray | None = None
    def fit(self, x: np.ndarray, y: np.ndarray) -> KNNClassifier:
        self.x_train_, self.y_train_ = x, y
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.x_train_ is not None and self.y_train_ is not None
        preds = []
        for row in x:
            dist = np.linalg.norm(self.x_train_ - row, axis=1)
            idx = np.argsort(dist)[: self.k]
            vals, counts = np.unique(self.y_train_[idx], return_counts=True)
            preds.append(vals[int(np.argmax(counts))])
        return np.asarray(preds)


@dataclass
class ThresholdClassifier:
    """Threshold a single feature (feature 0 after scaling) for binary tasks."""
    threshold_: float = 0.0
    classes_: np.ndarray | None = None
    def fit(self, x: np.ndarray, y: np.ndarray) -> ThresholdClassifier:
        self.classes_ = np.unique(y)
        self.threshold_ = float(np.median(x[:, 0]))
        return self
    def predict(self, x: np.ndarray) -> np.ndarray:
        assert self.classes_ is not None
        pos = self.classes_[-1]
        neg = self.classes_[0]
        return np.where(x[:, 0] >= self.threshold_, pos, neg)


REGRESSORS = {
    "mean": MeanRegressor,
    "linear_gd": LinearGDRegressor,
    "ridge": RidgeRegressor,
    "knn": KNNRegressor,
    "median": MedianRegressor,
}

CLASSIFIERS = {
    "majority": MajorityClassifier,
    "logistic_gd": LogisticGDClassifier,
    "knn": KNNClassifier,
    "threshold": ThresholdClassifier,
}


def create_model(name: str, task: str, **kwargs):
    table = REGRESSORS if task == "regression" else CLASSIFIERS
    if name not in table:
        raise ValueError(f"unknown model {name!r} for task {task}; options={sorted(table)}")
    return table[name](**kwargs)


def list_models(task: str) -> list[str]:
    return sorted((REGRESSORS if task == "regression" else CLASSIFIERS).keys())
