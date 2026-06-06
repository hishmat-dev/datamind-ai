from datamind.models.metric_window_10 import window_mean_10

def test_window_10():
    assert window_mean_10([1.0, 2.0, 3.0, 4.0]) > 0
