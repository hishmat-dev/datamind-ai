from datamind.models.metric_window_25 import window_mean_25

def test_window_25():
    assert window_mean_25([1.0, 2.0, 3.0, 4.0]) > 0
