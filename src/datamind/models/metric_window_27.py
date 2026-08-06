"""Rolling metric window helper 27."""
from __future__ import annotations

def window_mean_27(values: list[float], size: int = 5) -> float:
    if not values:
        return 0.0
    chunk = values[-size:]
    return sum(chunk) / len(chunk)
