"""Rolling metric window helper 31."""
from __future__ import annotations

def window_mean_31(values: list[float], size: int = 4) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
