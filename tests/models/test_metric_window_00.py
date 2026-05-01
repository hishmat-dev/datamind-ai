from datamind.models.metric_window_00 import window_mean_0

def test_window_0():
    assert window_mean_0([1.0, 2.0, 3.0, 4.0]) > 0
