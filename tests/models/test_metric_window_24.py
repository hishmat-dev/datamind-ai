from datamind.models.metric_window_24 import window_mean_24

def test_window_24():
    assert window_mean_24([1.0, 2.0, 3.0, 4.0]) > 0
