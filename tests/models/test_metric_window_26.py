from datamind.models.metric_window_26 import window_mean_26

def test_window_26():
    assert window_mean_26([1.0, 2.0, 3.0, 4.0]) > 0
