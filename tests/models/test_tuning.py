import numpy as np
from datamind.models.tuning import grid_search_linear_gd

def test_grid():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(100, 2))
    y = x @ np.array([1.0, 2.0])
    x = (x - x.mean(0)) / (x.std(0) + 1e-8)
    best = grid_search_linear_gd(x[:80], y[:80], x[80:], y[80:], n_iter=100)
    assert best["model"] is not None and best["rmse"] < 1.0
