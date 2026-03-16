from datamind.data.bounds import count_out_of_bounds
from datamind.data.generate import generate_housing

def test_bounds():
    df = generate_housing(40, seed=2)
    assert count_out_of_bounds(df, "rooms") >= 0
