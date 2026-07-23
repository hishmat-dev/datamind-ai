from datamind.models.metric_window_23 import window_mean_23

def test_window_23():
    assert window_mean_23([1.0, 2.0, 3.0, 4.0]) > 0
