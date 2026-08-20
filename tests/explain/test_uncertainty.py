import numpy as np
from datamind.explain.uncertainty import bootstrap_metric, prediction_interval, residual_std
from datamind.models.metrics import mae

def test_uncertainty():
    y = np.array([1.0, 2.0, 3.0, 4.0])
    pred = np.array([1.1, 1.9, 3.2, 3.8])
    sigma = residual_std(y, pred)
    low, high = prediction_interval(pred, sigma)
    assert np.all(low <= pred) and np.all(high >= pred)
    boot = bootstrap_metric(y, pred, mae, n_boot=50, seed=1)
    assert "mean" in boot and boot["p95"] >= boot["p05"]
