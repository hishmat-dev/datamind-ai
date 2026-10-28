"""Experiment runner: full train/eval + metadata record."""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
import numpy as np
import pandas as pd
from datamind.data.loader import load_dataset
from datamind.data.validator import validate_dataset
from datamind.evaluation.metrics import classification_metrics, regression_metrics
from datamind.features.split import train_test_split
from datamind.models.factory import create_model
from datamind.preprocessing.pipeline import PreprocessPipeline


@dataclass
class ExperimentResult:
    dataset: str
    task: str
    model: str
    metrics: dict
    n_train: int
    n_test: int
    seed: int
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    notes: str = ""
    validation_ok: bool = True

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, default=str)

    def save(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_json())
        return path


def run_experiment(
    dataset: str = "housing",
    model: str = "linear_gd",
    seed: int = 42,
    test_size: float = 0.2,
    notes: str = "",
) -> ExperimentResult:
    bundle = load_dataset(dataset, seed=seed)
    report = validate_dataset(bundle.frame, bundle.target, list(bundle.feature_cols))
    df = bundle.frame.copy()
    # drop rows with missing target
    df = df.dropna(subset=[bundle.target]).reset_index(drop=True)
    x = df[list(bundle.feature_cols)]
    y = df[bundle.target]
    # temporary frame for split helper
    tmp = x.copy()
    tmp[bundle.target] = y
    x_train, x_test, y_train, y_test = train_test_split(tmp, bundle.target, test_size=test_size, seed=seed)
    pipe = PreprocessPipeline().fit(x_train)
    xtr = pipe.transform(x_train).to_numpy(dtype=float)
    xte = pipe.transform(x_test).to_numpy(dtype=float)
    if bundle.task == "regression":
        ytr = y_train.to_numpy(dtype=float)
        yte = y_test.to_numpy(dtype=float)
    else:
        ytr = y_train.to_numpy()
        yte = y_test.to_numpy()
    est = create_model(model, bundle.task)
    est.fit(xtr, ytr)
    preds = est.predict(xte)
    if bundle.task == "regression":
        metrics = regression_metrics(yte, np.asarray(preds, dtype=float))
    else:
        score = None
        if hasattr(est, "predict_proba_positive"):
            score = est.predict_proba_positive(xte)
        elif hasattr(est, "decision_function"):
            score = est.decision_function(xte)
        metrics = classification_metrics(yte, preds, y_score=score)
    return ExperimentResult(
        dataset=dataset,
        task=bundle.task,
        model=model,
        metrics=metrics,
        n_train=len(x_train),
        n_test=len(x_test),
        seed=seed,
        notes=notes,
        validation_ok=report.ok,
    )
