from datamind.models.metric_window_39 import window_mean_39

def test_window_39():
    assert window_mean_39([1.0, 2.0, 3.0, 4.0]) > 0
