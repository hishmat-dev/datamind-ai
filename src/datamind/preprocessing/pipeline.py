"""Train-only-fit preprocessing: impute → scale → one-hot."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
import pandas as pd


@dataclass
class PreprocessPipeline:
    numeric_cols: list[str] = field(default_factory=list)
    categorical_cols: list[str] = field(default_factory=list)
    medians_: dict[str, float] = field(default_factory=dict)
    means_: dict[str, float] = field(default_factory=dict)
    stds_: dict[str, float] = field(default_factory=dict)
    categories_: dict[str, list[str]] = field(default_factory=dict)
    fitted_: bool = False

    def fit(self, x: pd.DataFrame) -> PreprocessPipeline:
        self.numeric_cols = [c for c in x.columns if pd.api.types.is_numeric_dtype(x[c])]
        self.categorical_cols = [c for c in x.columns if c not in self.numeric_cols]
        for c in self.numeric_cols:
            self.medians_[c] = float(x[c].median()) if x[c].notna().any() else 0.0
            filled = x[c].fillna(self.medians_[c])
            self.means_[c] = float(filled.mean())
            self.stds_[c] = float(filled.std(ddof=0)) or 1.0
        for c in self.categorical_cols:
            vals = sorted(x[c].astype(str).fillna("missing").unique().tolist())
            self.categories_[c] = vals
        self.fitted_ = True
        return self

    def transform(self, x: pd.DataFrame) -> pd.DataFrame:
        if not self.fitted_:
            raise RuntimeError("pipeline not fitted")
        out = pd.DataFrame(index=x.index)
        for c in self.numeric_cols:
            col = x[c] if c in x.columns else pd.Series(self.medians_[c], index=x.index)
            col = col.fillna(self.medians_[c])
            out[c] = (col - self.means_[c]) / self.stds_[c]
        for c in self.categorical_cols:
            raw = (x[c] if c in x.columns else pd.Series("missing", index=x.index)).astype(str).fillna("missing")
            for cat in self.categories_[c]:
                out[f"{c}__{cat}"] = (raw == cat).astype(float)
        return out

    def fit_transform(self, x: pd.DataFrame) -> pd.DataFrame:
        return self.fit(x).transform(x)
