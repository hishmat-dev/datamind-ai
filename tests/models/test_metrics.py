import numpy as np
from datamind.models.metrics import mae, mse, r2_score, regression_report, rmse

def test_metrics_perfect():
    y = np.array([1.0, 2.0, 3.0])
    assert mse(y, y) == 0.0
    assert rmse(y, y) == 0.0
    assert mae(y, y) == 0.0
    assert r2_score(y, y) == 1.0
    assert regression_report(y, y)["r2"] == 1.0
