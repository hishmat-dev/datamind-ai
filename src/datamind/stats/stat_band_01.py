"""Statistical band helper 1."""
from __future__ import annotations

def in_band_1(value: float, center: float = 1.0, width: float = 1.1) -> bool:
    return abs(value - center) <= width
