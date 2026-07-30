import numpy as np
from datamind.math.regularization import l1_penalty, l2_penalty, ridge_closed_form

def test_penalties_and_ridge():
    w = np.array([1.0, -2.0, 0.0])
    assert l2_penalty(w, 0.5) == 0.5 * 5.0
    assert l1_penalty(w, 0.5) == 0.5 * 3.0
    rng = np.random.default_rng(0)
    x = rng.normal(size=(100, 3))
    y = x @ np.array([1.0, 2.0, -1.0])
    w_hat = ridge_closed_form(x, y, alpha=0.1)
    assert w_hat.shape == (3,)
