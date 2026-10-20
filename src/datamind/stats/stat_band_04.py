"""Statistical band helper 4."""
from __future__ import annotations

def in_band_4(value: float, center: float = 4.0, width: float = 1.4) -> bool:
    return abs(value - center) <= width
