from __future__ import annotations

def should_stop(history: list[float], patience: int = 10, min_delta: float = 1e-6) -> bool:
    if len(history) < patience + 1:
        return False
    recent = history[-patience:]
    return (recent[0] - recent[-1]) < min_delta
