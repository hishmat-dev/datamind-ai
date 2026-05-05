"""Rolling metric window helper 1."""
from __future__ import annotations

def window_mean_1(values: list[float], size: int = 4) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
