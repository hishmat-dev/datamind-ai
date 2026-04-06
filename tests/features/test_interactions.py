from datamind.data.generate import generate_housing
from datamind.features.interactions import add_interaction

def test_interaction():
    df = add_interaction(generate_housing(20, seed=4), "rooms", "area_sqm")
    assert "rooms_x_area_sqm" in df.columns
