from datamind.models.metric_window_17 import window_mean_17

def test_window_17():
    assert window_mean_17([1.0, 2.0, 3.0, 4.0]) > 0
