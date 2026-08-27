"""Rolling metric window helper 33."""
from __future__ import annotations

def window_mean_33(values: list[float], size: int = 6) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
