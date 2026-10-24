"""Statistical band helper 5."""
from __future__ import annotations

def in_band_5(value: float, center: float = 5.0, width: float = 1.5) -> bool:
    return abs(value - center) <= width
