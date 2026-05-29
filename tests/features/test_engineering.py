from datamind.data.generate import generate_housing
from datamind.features.engineering import add_area_per_room, add_log_price, polynomial_features

def test_features():
    df = generate_housing(40, seed=7)
    df = add_area_per_room(df)
    df = add_log_price(df)
    df = polynomial_features(df, ["area_sqm"], degree=2)
    assert "area_per_room" in df.columns
    assert "log_price" in df.columns
    assert "area_sqm_sq" in df.columns
