from pathlib import Path
import numpy as np
from datamind.models.baselines import LinearRegressionGD
from datamind.models.persist import load_linear_model, save_linear_model

def test_save_load(tmp_path: Path):
    x = np.random.default_rng(1).normal(size=(50, 2))
    y = x @ np.array([1.0, 2.0])
    model = LinearRegressionGD(lr=0.1, n_iter=200).fit(x, y)
    save_linear_model(model, tmp_path)
    loaded = load_linear_model(tmp_path)
    assert np.allclose(loaded.predict(x), model.predict(x), atol=1e-6)
