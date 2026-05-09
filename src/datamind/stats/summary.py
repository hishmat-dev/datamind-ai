"""Statistical summaries for exploratory analysis."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass(frozen=True, slots=True)
class ColumnSummary:
    name: str
    count: int
    missing: int
    mean: float | None
    std: float | None
    min: float | None
    q25: float | None
    median: float | None
    q75: float | None
    max: float | None


def summarize_numeric(df: pd.DataFrame) -> list[ColumnSummary]:
    summaries: list[ColumnSummary] = []
    for col in df.select_dtypes(include=[np.number]).columns:
        s = df[col]
        summaries.append(
            ColumnSummary(
                name=str(col),
                count=int(s.notna().sum()),
                missing=int(s.isna().sum()),
                mean=float(s.mean()) if s.notna().any() else None,
                std=float(s.std(ddof=0)) if s.notna().any() else None,
                min=float(s.min()) if s.notna().any() else None,
                q25=float(s.quantile(0.25)) if s.notna().any() else None,
                median=float(s.median()) if s.notna().any() else None,
                q75=float(s.quantile(0.75)) if s.notna().any() else None,
                max=float(s.max()) if s.notna().any() else None,
            )
        )
    return summaries


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=[np.number]).corr(numeric_only=True)
