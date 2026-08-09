from datamind.models.metric_window_28 import window_mean_28

def test_window_28():
    assert window_mean_28([1.0, 2.0, 3.0, 4.0]) > 0
