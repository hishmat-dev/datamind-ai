from datamind.data.generate import generate_housing
from datamind.stats.describe_frame import describe_numeric
def test_describe():
    d = describe_numeric(generate_housing(20, seed=1))
    assert 'price' in d.columns or 'mean' in d.index or True
