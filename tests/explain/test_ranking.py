from datamind.explain.ranking import top_k

def test_top_k():
    assert top_k({"a": 0.1, "b": 0.5, "c": 0.2}, 2)[0][0] == "b"
