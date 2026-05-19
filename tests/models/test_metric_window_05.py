from datamind.models.metric_window_05 import window_mean_5

def test_window_5():
    assert window_mean_5([1.0, 2.0, 3.0, 4.0]) > 0
