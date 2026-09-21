from __future__ import annotations
import json
from pathlib import Path

def save_metrics(path: Path, metrics: dict[str, float]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metrics, indent=2))
    return path

def load_metrics(path: Path) -> dict[str, float]:
    return {k: float(v) for k, v in json.loads(path.read_text()).items()}
