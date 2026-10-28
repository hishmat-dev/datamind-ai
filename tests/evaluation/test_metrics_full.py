import numpy as np
from datamind.evaluation.metrics import classification_metrics, regression_metrics, roc_auc_binary

def test_regression_metrics():
    y = np.array([1.0, 2.0, 3.0])
    m = regression_metrics(y, y)
    assert m["mae"] == 0 and m["r2"] == 1

def test_classification_metrics():
    y = np.array([0, 0, 1, 1])
    p = np.array([0, 1, 1, 1])
    m = classification_metrics(y, p, y_score=np.array([0.1, 0.4, 0.6, 0.9]))
    assert "accuracy" in m and "f1" in m and "confusion_matrix" in m
    assert m["roc_auc"] >= 0.5
