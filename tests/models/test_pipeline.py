import numpy as np
from datamind.data.clean import impute_numeric_median
from datamind.data.generate import generate_housing
from datamind.features.engineering import add_area_per_room
from datamind.features.split import train_test_split
from datamind.models.pipeline import dataframe_to_xy, train_linear_gd, train_mean_baseline

def test_pipeline_mean_and_linear():
    df = impute_numeric_median(add_area_per_room(generate_housing(150, seed=10)))
    x_train, x_test, y_train, y_test = train_test_split(df, "price", seed=10)
    cols = list(x_train.select_dtypes(include=[np.number]).columns)
    xtr, ytr = dataframe_to_xy(x_train, y_train, cols)
    xte, yte = dataframe_to_xy(x_test, y_test, cols)
    mu, sig = xtr.mean(0), xtr.std(0) + 1e-8
    xtr, xte = (xtr - mu) / sig, (xte - mu) / sig
    mean_res = train_mean_baseline(xtr, ytr, xte, yte)
    lin_res = train_linear_gd(xtr, ytr, xte, yte, lr=0.05, n_iter=300)
    assert "rmse" in mean_res.metrics
    assert lin_res.metrics["r2"] >= mean_res.metrics["r2"] - 0.05
