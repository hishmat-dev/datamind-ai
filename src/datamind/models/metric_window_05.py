"""Rolling metric window helper 5."""
from __future__ import annotations

def window_mean_5(values: list[float], size: int = 3) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
