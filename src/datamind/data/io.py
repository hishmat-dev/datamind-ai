"""Load and save datasets."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
from datamind.core.config import get_settings
from datamind.data.generate import generate_housing
from datamind.data.validate import assert_valid


def ensure_sample_dataset(path: Path | None = None, n_samples: int = 500, seed: int = 42) -> Path:
    settings = get_settings()
    path = path or (settings.data_raw_dir / "housing.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        df = generate_housing(n_samples=n_samples, seed=seed)
        df.to_csv(path, index=False)
    return path


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    assert_valid(df)
    return df


def save_processed(df: pd.DataFrame, name: str = "housing_clean.csv") -> Path:
    settings = get_settings()
    settings.data_processed_dir.mkdir(parents=True, exist_ok=True)
    out = settings.data_processed_dir / name
    df.to_csv(out, index=False)
    return out
