from datamind.models.metric_window_15 import window_mean_15

def test_window_15():
    assert window_mean_15([1.0, 2.0, 3.0, 4.0]) > 0
