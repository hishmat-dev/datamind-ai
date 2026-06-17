from datamind.models.metric_window_13 import window_mean_13

def test_window_13():
    assert window_mean_13([1.0, 2.0, 3.0, 4.0]) > 0
