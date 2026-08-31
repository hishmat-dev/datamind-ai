from datamind.models.metric_window_34 import window_mean_34

def test_window_34():
    assert window_mean_34([1.0, 2.0, 3.0, 4.0]) > 0
