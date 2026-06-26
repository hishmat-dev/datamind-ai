import numpy as np
from datamind.models.baselines import LinearRegressionGD, MeanBaseline
from datamind.models.metrics import r2_score

def test_mean_baseline():
    x = np.ones((20, 2))
    y = np.arange(20, dtype=float)
    m = MeanBaseline().fit(x, y)
    preds = m.predict(x)
    assert np.allclose(preds, y.mean())

def test_linear_gd_learns():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(200, 3))
    true_w = np.array([1.5, -2.0, 0.5])
    y = x @ true_w + 0.1 * rng.normal(size=200)
    # standardize
    x = (x - x.mean(0)) / (x.std(0) + 1e-8)
    model = LinearRegressionGD(lr=0.1, n_iter=800).fit(x, y)
    preds = model.predict(x)
    assert r2_score(y, preds) > 0.9
