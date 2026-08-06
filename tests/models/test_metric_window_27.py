from datamind.models.metric_window_27 import window_mean_27

def test_window_27():
    assert window_mean_27([1.0, 2.0, 3.0, 4.0]) > 0
