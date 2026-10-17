"""Statistical band helper 3."""
from __future__ import annotations

def in_band_3(value: float, center: float = 3.0, width: float = 1.3) -> bool:
    return abs(value - center) <= width
