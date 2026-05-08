from datamind.models.metric_window_02 import window_mean_2

def test_window_2():
    assert window_mean_2([1.0, 2.0, 3.0, 4.0]) > 0
