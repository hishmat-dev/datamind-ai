"""Rolling metric window helper 39."""
from __future__ import annotations

def window_mean_39(values: list[float], size: int = 7) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
