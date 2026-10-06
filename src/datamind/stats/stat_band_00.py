"""Statistical band helper 0."""
from __future__ import annotations

def in_band_0(value: float, center: float = 0.0, width: float = 1.0) -> bool:
    return abs(value - center) <= width
