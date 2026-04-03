"""Rank features by importance scores."""
from __future__ import annotations

def top_k(importances: dict[str, float], k: int = 5) -> list[tuple[str, float]]:
    items = sorted(importances.items(), key=lambda kv: abs(kv[1]), reverse=True)
    return items[:k]
