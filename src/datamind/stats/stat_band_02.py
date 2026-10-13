"""Statistical band helper 2."""
from __future__ import annotations

def in_band_2(value: float, center: float = 2.0, width: float = 1.2) -> bool:
    return abs(value - center) <= width
