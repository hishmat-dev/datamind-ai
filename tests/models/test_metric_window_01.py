from datamind.models.metric_window_01 import window_mean_1

def test_window_1():
    assert window_mean_1([1.0, 2.0, 3.0, 4.0]) > 0
