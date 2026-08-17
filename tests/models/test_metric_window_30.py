from datamind.models.metric_window_30 import window_mean_30

def test_window_30():
    assert window_mean_30([1.0, 2.0, 3.0, 4.0]) > 0
