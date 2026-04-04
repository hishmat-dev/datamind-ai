"""Generate synthetic research datasets with a fixed seed."""
from __future__ import annotations
import numpy as np
import pandas as pd
from datamind.data.schema import HOUSING_SCHEMA


def generate_housing(n_samples: int = 500, seed: int = 42) -> pd.DataFrame:
    """Create a synthetic housing dataset for reproducible experiments."""
    rng = np.random.default_rng(seed)
    rooms = rng.integers(1, 8, size=n_samples).astype(float)
    area = rng.normal(90, 25, size=n_samples).clip(25, 250)
    age = rng.exponential(15, size=n_samples).clip(0, 80)
    distance = rng.exponential(8, size=n_samples).clip(0.2, 40)
    crime = rng.beta(2, 5, size=n_samples)
    school = rng.uniform(3, 10, size=n_samples)
    noise = rng.normal(0, 15_000, size=n_samples)
    price = (
        40_000
        + rooms * 25_000
        + area * 1_200
        - age * 800
        - distance * 3_500
        - crime * 40_000
        + school * 8_000
        + noise
    ).clip(30_000, None)
    df = pd.DataFrame(
        {
            "rooms": rooms,
            "area_sqm": area,
            "age_years": age,
            "distance_km": distance,
            "crime_index": crime,
            "school_score": school,
            "price": price,
        }
    )
    # Inject a few missing values for cleaning exercises
    miss_idx = rng.choice(n_samples, size=max(1, n_samples // 50), replace=False)
    df.loc[miss_idx, "age_years"] = np.nan
    return df


def schema_columns() -> list[str]:
    return HOUSING_SCHEMA.column_names()
