from datamind.models.metric_window_18 import window_mean_18

def test_window_18():
    assert window_mean_18([1.0, 2.0, 3.0, 4.0]) > 0
