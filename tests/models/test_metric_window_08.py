from datamind.models.metric_window_08 import window_mean_8

def test_window_8():
    assert window_mean_8([1.0, 2.0, 3.0, 4.0]) > 0
