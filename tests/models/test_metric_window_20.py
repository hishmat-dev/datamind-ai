from datamind.models.metric_window_20 import window_mean_20

def test_window_20():
    assert window_mean_20([1.0, 2.0, 3.0, 4.0]) > 0
