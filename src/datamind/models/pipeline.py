"""Training pipeline helpers."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd
from datamind.models.baselines import LinearRegressionGD, MeanBaseline
from datamind.models.metrics import regression_report


@dataclass
class TrainResult:
    model_name: str
    metrics: dict[str, float]
    model: object


def dataframe_to_xy(
    x: pd.DataFrame, y: pd.Series, feature_cols: list[str] | None = None
) -> tuple[np.ndarray, np.ndarray]:
    cols = feature_cols or list(x.select_dtypes(include=[np.number]).columns)
    return x[cols].to_numpy(dtype=float), y.to_numpy(dtype=float)


def train_mean_baseline(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray, y_test: np.ndarray) -> TrainResult:
    model = MeanBaseline().fit(x_train, y_train)
    preds = model.predict(x_test)
    return TrainResult("mean_baseline", regression_report(y_test, preds), model)


def train_linear_gd(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    lr: float = 0.01,
    n_iter: int = 500,
    l2: float = 0.0,
) -> TrainResult:
    model = LinearRegressionGD(lr=lr, n_iter=n_iter, l2=l2).fit(x_train, y_train)
    preds = model.predict(x_test)
    return TrainResult("linear_gd", regression_report(y_test, preds), model)
