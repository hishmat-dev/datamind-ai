"""Model persistence using numpy and json metadata."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from datamind.models.baselines import LinearRegressionGD


def save_linear_model(model: LinearRegressionGD, directory: Path, name: str = "linear_gd") -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    if model.weights_ is None:
        raise RuntimeError("model not fitted")
    np.save(directory / f"{name}_weights.npy", model.weights_)
    meta = {
        "bias": model.bias_,
        "lr": model.lr,
        "n_iter": model.n_iter,
        "l2": model.l2,
        "loss_final": model.loss_history_[-1] if model.loss_history_ else None,
    }
    path = directory / f"{name}_meta.json"
    path.write_text(json.dumps(meta, indent=2))
    return path


def load_linear_model(directory: Path, name: str = "linear_gd") -> LinearRegressionGD:
    weights = np.load(directory / f"{name}_weights.npy")
    meta = json.loads((directory / f"{name}_meta.json").read_text())
    model = LinearRegressionGD(lr=meta["lr"], n_iter=meta["n_iter"], l2=meta["l2"])
    model.weights_ = weights
    model.bias_ = float(meta["bias"])
    return model
