from datamind.models.metric_window_14 import window_mean_14

def test_window_14():
    assert window_mean_14([1.0, 2.0, 3.0, 4.0]) > 0
