import numpy as np
from datamind.models.factory import create_model, list_models

def test_regressor_count():
    assert len(list_models("regression")) >= 5

def test_classifier_count():
    assert len(list_models("classification")) >= 4

def test_ridge_fit():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(60, 3))
    y = x @ np.array([1.0, 2.0, -1.0])
    m = create_model("ridge", "regression", alpha=0.1).fit(x, y)
    assert m.predict(x).shape == (60,)
