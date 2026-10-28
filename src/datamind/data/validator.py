"""Dataset quality checks: missing, duplicates, outliers, leakage."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
import pandas as pd


@dataclass
class ValidationReport:
    n_rows: int
    n_cols: int
    missing_frac: dict[str, float] = field(default_factory=dict)
    n_duplicates: int = 0
    outlier_counts: dict[str, int] = field(default_factory=dict)
    leakage_flags: list[str] = field(default_factory=list)
    ok: bool = True


def _iqr_outliers(s: pd.Series) -> int:
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    if iqr == 0 or np.isnan(iqr):
        return 0
    mask = (s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)
    return int(mask.sum())


def validate_dataset(
    df: pd.DataFrame,
    target: str,
    feature_cols: list[str] | tuple[str, ...],
) -> ValidationReport:
    report = ValidationReport(n_rows=len(df), n_cols=len(df.columns))
    for c in df.columns:
        report.missing_frac[str(c)] = float(df[c].isna().mean())
    report.n_duplicates = int(df.duplicated().sum())
    for c in feature_cols:
        if c in df.columns and pd.api.types.is_numeric_dtype(df[c]):
            report.outlier_counts[str(c)] = _iqr_outliers(df[c].dropna())
    # leakage: target identical to a feature, or perfect correlation
    if target in df.columns:
        for c in feature_cols:
            if c not in df.columns or c == target:
                continue
            if pd.api.types.is_numeric_dtype(df[c]) and pd.api.types.is_numeric_dtype(df[target]):
                corr = df[[c, target]].corr().iloc[0, 1]
                if corr == 1.0 or corr == -1.0:
                    report.leakage_flags.append(f"perfect correlation {c}↔{target}")
            if df[c].astype(str).equals(df[target].astype(str)):
                report.leakage_flags.append(f"feature {c} identical to target")
    if report.n_duplicates > len(df) * 0.5:
        report.ok = False
    if report.leakage_flags:
        report.ok = False
    return report
