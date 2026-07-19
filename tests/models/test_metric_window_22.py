from datamind.models.metric_window_22 import window_mean_22

def test_window_22():
    assert window_mean_22([1.0, 2.0, 3.0, 4.0]) > 0
