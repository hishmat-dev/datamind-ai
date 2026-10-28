import numpy as np
from datamind.optimization.ols import closed_form_ols, compare_ols_to_gd

def test_ols_vs_gd():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(100, 2))
    y = x @ np.array([1.5, -0.5]) + 0.01 * rng.normal(size=100)
    x = (x - x.mean(0)) / (x.std(0) + 1e-8)
    ols = closed_form_ols(x, y)
    assert ols.weights.shape == (2,)
    stats = compare_ols_to_gd(x, y, lr=0.1, n_iter=500)
    assert stats["mse_gd"] < 0.1
