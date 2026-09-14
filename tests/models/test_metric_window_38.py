from datamind.models.metric_window_38 import window_mean_38

def test_window_38():
    assert window_mean_38([1.0, 2.0, 3.0, 4.0]) > 0
