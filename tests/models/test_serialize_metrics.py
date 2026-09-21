from pathlib import Path
from datamind.models.serialize_metrics import load_metrics, save_metrics
def test_ser(tmp_path: Path):
    p = save_metrics(tmp_path / 'm.json', {'r2': 0.9})
    assert load_metrics(p)['r2'] == 0.9
