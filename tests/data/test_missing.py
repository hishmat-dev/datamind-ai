from datamind.data.generate import generate_housing
from datamind.data.missing import columns_with_missing, missing_report

def test_missing():
    df = generate_housing(50, seed=1)
    report = missing_report(df)
    assert "age_years" in report
    assert "age_years" in columns_with_missing(df)
