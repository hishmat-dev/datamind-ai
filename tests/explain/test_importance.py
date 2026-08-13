import numpy as np
from datamind.explain.importance import linear_coefficient_importance, permutation_importance
from datamind.models.baselines import LinearRegressionGD

def test_importances():
    names = ["a", "b"]
    imp = linear_coefficient_importance(np.array([2.0, 1.0]), names)
    assert abs(imp["a"] - 2 / 3) < 1e-9
    rng = np.random.default_rng(0)
    x = rng.normal(size=(80, 2))
    y = x @ np.array([3.0, 0.1])
    model = LinearRegressionGD(lr=0.1, n_iter=400).fit(x, y)
    pimp = permutation_importance(model.predict, x, y, names, seed=0)
    assert pimp["a"] > pimp["b"]
