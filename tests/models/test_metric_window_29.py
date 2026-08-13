from datamind.models.metric_window_29 import window_mean_29

def test_window_29():
    assert window_mean_29([1.0, 2.0, 3.0, 4.0]) > 0
