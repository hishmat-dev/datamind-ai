from pathlib import Path
from datamind.analytics.reports import write_metrics_report

def test_report(tmp_path: Path):
    path = write_metrics_report(tmp_path / "r.md", "Run", {"rmse": 1.5, "r2": 0.8})
    text = path.read_text()
    assert "rmse" in text and "0.800000" in text
