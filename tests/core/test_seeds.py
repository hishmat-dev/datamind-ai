from datamind.core.seeds import make_rng
def test_seed():
    assert make_rng(1).integers(0, 100) == make_rng(1).integers(0, 100)
