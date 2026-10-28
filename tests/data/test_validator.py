from datamind.data.loader import load_dataset
from datamind.data.validator import validate_dataset

def test_validate_housing():
    b = load_dataset("housing", n_samples=80, seed=0)
    report = validate_dataset(b.frame, b.target, list(b.feature_cols))
    assert report.n_rows == 80
    assert "age_years" in report.missing_frac
