from datamind.data.generate import generate_housing
from datamind.features.names import numeric_columns
def test_names():
    assert 'price' in numeric_columns(generate_housing(10, seed=1))
