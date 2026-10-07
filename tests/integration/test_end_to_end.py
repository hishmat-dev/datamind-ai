"""End-to-end: generate → clean → features → train → explain → sql."""
from pathlib import Path
import numpy as np
from datamind.analytics.sql_store import connect, init_schema, load_dataframe, record_experiment
from datamind.data.clean import impute_numeric_median
from datamind.data.generate import generate_housing
from datamind.explain.importance import linear_coefficient_importance
from datamind.features.engineering import add_area_per_room
from datamind.features.split import train_test_split
from datamind.models.pipeline import dataframe_to_xy, train_linear_gd

def test_e2e(tmp_path: Path):
    df = impute_numeric_median(add_area_per_room(generate_housing(120, seed=12)))
    x_train, x_test, y_train, y_test = train_test_split(df, "price", seed=12)
    cols = list(x_train.select_dtypes(include=[np.number]).columns)
    xtr, ytr = dataframe_to_xy(x_train, y_train, cols)
    xte, yte = dataframe_to_xy(x_test, y_test, cols)
    mu, sig = xtr.mean(0), xtr.std(0) + 1e-8
    result = train_linear_gd((xtr - mu) / sig, ytr, (xte - mu) / sig, yte, lr=0.05, n_iter=250)
    assert result.metrics["r2"] > 0.3
    assert result.model.weights_ is not None
    imp = linear_coefficient_importance(result.model.weights_, cols)
    assert set(imp) == set(cols)
    conn = connect(tmp_path / "e2e.db")
    init_schema(conn)
    load_dataframe(conn, df)
    record_experiment(conn, result.model_name, result.metrics["rmse"], result.metrics["mae"], result.metrics["r2"])
    conn.close()
