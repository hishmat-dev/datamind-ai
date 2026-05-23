from datamind.models.metric_window_06 import window_mean_6

def test_window_6():
    assert window_mean_6([1.0, 2.0, 3.0, 4.0]) > 0
