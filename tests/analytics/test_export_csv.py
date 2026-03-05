from pathlib import Path
from datamind.analytics.export_csv import export_csv
from datamind.data.generate import generate_housing
def test_export(tmp_path: Path):
    p = export_csv(generate_housing(5, seed=1), tmp_path / 'o.csv')
    assert p.exists()
