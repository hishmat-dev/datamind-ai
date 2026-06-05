from datamind.data.generate import generate_housing
from datamind.features.split import train_test_split

def test_split_reproducible():
    df = generate_housing(100, seed=8)
    a = train_test_split(df, "price", test_size=0.25, seed=99)
    b = train_test_split(df, "price", test_size=0.25, seed=99)
    assert list(a[2]) == list(b[2])
    assert len(a[1]) == 25
