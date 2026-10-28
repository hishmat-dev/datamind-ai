"""Regression and classification metrics."""
from __future__ import annotations
import numpy as np


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(mse(y_true, y_pred)))


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    return 0.0 if ss_tot == 0 else 1.0 - ss_res / ss_tot


def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    return {"mae": mae(y_true, y_pred), "rmse": rmse(y_true, y_pred), "r2": r2_score(y_true, y_pred)}


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(y_true == y_pred))


def _binary_counts(y_true: np.ndarray, y_pred: np.ndarray, positive) -> tuple[int, int, int, int]:
    tp = int(np.sum((y_true == positive) & (y_pred == positive)))
    fp = int(np.sum((y_true != positive) & (y_pred == positive)))
    fn = int(np.sum((y_true == positive) & (y_pred != positive)))
    tn = int(np.sum((y_true != positive) & (y_pred != positive)))
    return tp, fp, fn, tn


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    labels = np.unique(y_true)
    if len(labels) == 0:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}
    # macro average
    precs, recs, f1s = [], [], []
    for lab in labels:
        tp, fp, fn, _ = _binary_counts(y_true, y_pred, lab)
        p = tp / (tp + fp) if (tp + fp) else 0.0
        r = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) else 0.0
        precs.append(p); recs.append(r); f1s.append(f1)
    return {
        "precision": float(np.mean(precs)),
        "recall": float(np.mean(recs)),
        "f1": float(np.mean(f1s)),
    }


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    labels = sorted(set(y_true) | set(y_pred), key=lambda x: str(x))
    idx = {lab: i for i, lab in enumerate(labels)}
    cm = np.zeros((len(labels), len(labels)), dtype=int)
    for t, p in zip(y_true, y_pred, strict=True):
        cm[idx[t], idx[p]] += 1
    return cm


def roc_auc_binary(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """AUC via Mann–Whitney on binary labels {0,1} or two unique labels."""
    labels = np.unique(y_true)
    if len(labels) != 2:
        return float("nan")
    pos, neg = labels[1], labels[0]
    scores_pos = y_score[y_true == pos]
    scores_neg = y_score[y_true == neg]
    if len(scores_pos) == 0 or len(scores_neg) == 0:
        return float("nan")
    # pairwise
    correct = 0.0
    for sp in scores_pos:
        correct += float(np.sum(sp > scores_neg)) + 0.5 * float(np.sum(sp == scores_neg))
    return correct / (len(scores_pos) * len(scores_neg))


def classification_metrics(
    y_true: np.ndarray, y_pred: np.ndarray, y_score: np.ndarray | None = None
) -> dict[str, float | list]:
    out: dict[str, float | list] = {"accuracy": accuracy(y_true, y_pred)}
    out.update(precision_recall_f1(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    out["confusion_matrix"] = cm.tolist()
    if y_score is not None and len(np.unique(y_true)) == 2:
        out["roc_auc"] = roc_auc_binary(y_true, y_score)
    return out
