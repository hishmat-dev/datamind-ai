from datamind.models.metric_window_04 import window_mean_4

def test_window_4():
    assert window_mean_4([1.0, 2.0, 3.0, 4.0]) > 0
