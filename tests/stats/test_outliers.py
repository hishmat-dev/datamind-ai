from datamind.data.generate import generate_housing
from datamind.stats.outliers import outlier_report

def test_outlier_report():
    df = generate_housing(100, seed=6)
    report = outlier_report(df, "price")
    assert report["n"] == 100
    assert "iqr_outliers" in report
