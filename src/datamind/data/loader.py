"""Load classic research datasets (bundled synthetic analogs for offline use)."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass(frozen=True, slots=True)
class DatasetBundle:
    name: str
    frame: pd.DataFrame
    target: str
    task: str  # regression | classification
    feature_cols: tuple[str, ...]
    license_note: str


def _housing(n: int = 400, seed: int = 42) -> DatasetBundle:
    rng = np.random.default_rng(seed)
    rooms = rng.integers(1, 8, n).astype(float)
    area = rng.normal(90, 25, n).clip(25, 250)
    age = rng.exponential(15, n).clip(0, 80)
    dist = rng.exponential(8, n).clip(0.2, 40)
    crime = rng.beta(2, 5, n)
    school = rng.uniform(3, 10, n)
    price = (40_000 + rooms * 25_000 + area * 1_200 - age * 800 - dist * 3_500
             - crime * 40_000 + school * 8_000 + rng.normal(0, 12_000, n)).clip(30_000)
    df = pd.DataFrame({
        "rooms": rooms, "area_sqm": area, "age_years": age, "distance_km": dist,
        "crime_index": crime, "school_score": school, "price": price,
    })
    miss = rng.choice(n, size=max(1, n // 40), replace=False)
    df.loc[miss, "age_years"] = np.nan
    feats = ("rooms", "area_sqm", "age_years", "distance_km", "crime_index", "school_score")
    return DatasetBundle("housing", df, "price", "regression", feats,
                         "Synthetic analog of tabular housing data for offline research.")


def _diabetes(n: int = 400, seed: int = 42) -> DatasetBundle:
    rng = np.random.default_rng(seed + 1)
    age = rng.uniform(20, 80, n)
    bmi = rng.normal(28, 5, n).clip(18, 45)
    bp = rng.normal(90, 12, n).clip(60, 130)
    s1 = rng.normal(150, 30, n)
    s2 = rng.normal(100, 20, n)
    s3 = rng.normal(50, 15, n)
    target = (0.3 * age + 2.5 * bmi + 0.8 * bp + 0.1 * s1 - 0.05 * s2 + 0.2 * s3
              + rng.normal(0, 15, n))
    df = pd.DataFrame({"age": age, "bmi": bmi, "bp": bp, "s1": s1, "s2": s2, "s3": s3, "disease_progress": target})
    feats = ("age", "bmi", "bp", "s1", "s2", "s3")
    return DatasetBundle("diabetes", df, "disease_progress", "regression", feats,
                         "Synthetic analog inspired by diabetes progression tables.")


def _iris(n: int = 150, seed: int = 42) -> DatasetBundle:
    rng = np.random.default_rng(seed + 2)
    centers = {
        "setosa": (5.0, 3.4, 1.5, 0.2),
        "versicolor": (6.0, 2.8, 4.3, 1.3),
        "virginica": (6.5, 3.0, 5.5, 2.0),
    }
    rows = []
    for label, (sl, sw, pl, pw) in centers.items():
        for _ in range(n // 3):
            rows.append({
                "sepal_length": sl + rng.normal(0, 0.3),
                "sepal_width": sw + rng.normal(0, 0.25),
                "petal_length": pl + rng.normal(0, 0.3),
                "petal_width": pw + rng.normal(0, 0.2),
                "species": label,
            })
    df = pd.DataFrame(rows)
    feats = ("sepal_length", "sepal_width", "petal_length", "petal_width")
    return DatasetBundle("iris", df, "species", "classification", feats,
                         "Synthetic analog of the Iris flower dataset.")


def _wine(n: int = 180, seed: int = 42) -> DatasetBundle:
    rng = np.random.default_rng(seed + 3)
    rows = []
    for cls, (a, b, c) in enumerate([(13.0, 2.0, 2.5), (12.2, 2.5, 2.2), (13.5, 1.8, 2.8)], start=1):
        for _ in range(n // 3):
            rows.append({
                "alcohol": a + rng.normal(0, 0.4),
                "malic_acid": b + rng.normal(0, 0.3),
                "ash": c + rng.normal(0, 0.2),
                "flavanoids": rng.normal(2.0 + cls * 0.3, 0.4),
                "color_intensity": rng.normal(4.0 + cls, 0.8),
                "class": cls,
            })
    df = pd.DataFrame(rows)
    feats = ("alcohol", "malic_acid", "ash", "flavanoids", "color_intensity")
    return DatasetBundle("wine", df, "class", "classification", feats,
                         "Synthetic analog of the Wine recognition dataset.")


DATASETS = {
    "housing": _housing,
    "diabetes": _diabetes,
    "iris": _iris,
    "wine": _wine,
}


def list_datasets() -> list[str]:
    return sorted(DATASETS)


def load_dataset(name: str, n_samples: int | None = None, seed: int = 42) -> DatasetBundle:
    if name not in DATASETS:
        raise ValueError(f"unknown dataset {name!r}; choose from {list_datasets()}")
    kwargs = {}
    if n_samples is not None:
        kwargs["n"] = n_samples
    kwargs["seed"] = seed
    return DATASETS[name](**kwargs)
