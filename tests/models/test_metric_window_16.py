from datamind.models.metric_window_16 import window_mean_16

def test_window_16():
    assert window_mean_16([1.0, 2.0, 3.0, 4.0]) > 0
