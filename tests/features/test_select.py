from datamind.data.generate import generate_housing
from datamind.features.select import drop_highly_correlated, high_variance_columns

def test_select():
    df = generate_housing(50, seed=5)
    assert "price" in high_variance_columns(df)
    assert isinstance(drop_highly_correlated(df), list)
