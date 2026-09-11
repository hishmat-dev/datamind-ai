from datamind.models.metric_window_37 import window_mean_37

def test_window_37():
    assert window_mean_37([1.0, 2.0, 3.0, 4.0]) > 0
