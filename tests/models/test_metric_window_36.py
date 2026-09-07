from datamind.models.metric_window_36 import window_mean_36

def test_window_36():
    assert window_mean_36([1.0, 2.0, 3.0, 4.0]) > 0
