from datamind.models.metric_window_35 import window_mean_35

def test_window_35():
    assert window_mean_35([1.0, 2.0, 3.0, 4.0]) > 0
