"""Dataset schema definitions and column contracts."""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ColumnSpec:
    name: str
    dtype: str  # float, int, category, string
    nullable: bool = True
    description: str = ""


@dataclass(frozen=True, slots=True)
class DatasetSchema:
    name: str
    columns: tuple[ColumnSpec, ...]
    target: str | None = None
    license_note: str = "Synthetic educational data; not for production claims."

    def column_names(self) -> list[str]:
        return [c.name for c in self.columns]

    def required_columns(self) -> list[str]:
        return [c.name for c in self.columns if not c.nullable]


# Default research dataset: housing-like regression problem
HOUSING_SCHEMA = DatasetSchema(
    name="synthetic_housing",
    target="price",
    columns=(
        ColumnSpec("rooms", "float", False, "Number of rooms"),
        ColumnSpec("area_sqm", "float", False, "Floor area in square meters"),
        ColumnSpec("age_years", "float", True, "Building age"),
        ColumnSpec("distance_km", "float", True, "Distance to city center"),
        ColumnSpec("crime_index", "float", True, "Normalized crime index 0-1"),
        ColumnSpec("school_score", "float", True, "Local school quality 0-10"),
        ColumnSpec("price", "float", False, "Sale price (target)"),
    ),
)
