from datamind.models.metric_window_07 import window_mean_7

def test_window_7():
    assert window_mean_7([1.0, 2.0, 3.0, 4.0]) > 0
