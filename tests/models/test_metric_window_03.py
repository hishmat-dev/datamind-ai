from datamind.models.metric_window_03 import window_mean_3

def test_window_3():
    assert window_mean_3([1.0, 2.0, 3.0, 4.0]) > 0
