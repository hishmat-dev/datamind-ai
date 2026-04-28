from datamind.models.early_stop import should_stop
def test_es():
    assert not should_stop([1, 0.9, 0.8], patience=5)
    assert should_stop([1.0] + [0.99] * 12, patience=10, min_delta=0.1)
