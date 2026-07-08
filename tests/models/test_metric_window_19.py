from datamind.models.metric_window_19 import window_mean_19

def test_window_19():
    assert window_mean_19([1.0, 2.0, 3.0, 4.0]) > 0
