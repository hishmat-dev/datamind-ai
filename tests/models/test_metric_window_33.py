from datamind.models.metric_window_33 import window_mean_33

def test_window_33():
    assert window_mean_33([1.0, 2.0, 3.0, 4.0]) > 0
