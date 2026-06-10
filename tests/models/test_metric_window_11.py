from datamind.models.metric_window_11 import window_mean_11

def test_window_11():
    assert window_mean_11([1.0, 2.0, 3.0, 4.0]) > 0
