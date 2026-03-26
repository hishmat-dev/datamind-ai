from datamind.data.generate import generate_housing
from datamind.data.shape import shape_tuple
def test_shape():
    assert shape_tuple(generate_housing(12, seed=1))[0] == 12
