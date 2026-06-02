from datamind.models.metric_window_09 import window_mean_9

def test_window_9():
    assert window_mean_9([1.0, 2.0, 3.0, 4.0]) > 0
