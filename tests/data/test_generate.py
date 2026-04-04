from datamind.data.generate import generate_housing, schema_columns
from datamind.data.validate import validate_dataframe

def test_generate_shape_and_schema():
    df = generate_housing(n_samples=100, seed=0)
    assert len(df) == 100
    assert list(df.columns) == schema_columns()
    assert validate_dataframe(df) == []
