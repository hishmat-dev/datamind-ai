from datamind.data.generate import generate_housing
from datamind.data.sample import head_sample
def test_sample():
    assert len(head_sample(generate_housing(10, seed=1), 3)) == 3
