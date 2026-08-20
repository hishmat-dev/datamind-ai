from datamind.models.metric_window_31 import window_mean_31

def test_window_31():
    assert window_mean_31([1.0, 2.0, 3.0, 4.0]) > 0
