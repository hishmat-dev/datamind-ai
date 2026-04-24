from datamind.models.compare import best_model, rank_by_metric
from datamind.models.pipeline import TrainResult

def test_compare():
    a = TrainResult("a", {"rmse": 2.0, "r2": 0.5}, model=None)
    b = TrainResult("b", {"rmse": 1.0, "r2": 0.8}, model=None)
    assert rank_by_metric([a, b], "rmse")[0].model_name == "b"
    assert best_model([a, b], "r2").model_name == "b"
