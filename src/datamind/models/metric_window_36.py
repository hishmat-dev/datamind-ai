"""Rolling metric window helper 36."""
from __future__ import annotations

def window_mean_36(values: list[float], size: int = 4) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
