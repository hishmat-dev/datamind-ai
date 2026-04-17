"""Learning-rate schedules for educational GD."""
from __future__ import annotations

def constant(lr: float, step: int) -> float:
    return lr

def step_decay(lr: float, step: int, drop_every: int = 100, factor: float = 0.5) -> float:
    return lr * (factor ** (step // drop_every))

def inverse_time(lr: float, step: int, decay: float = 0.01) -> float:
    return lr / (1.0 + decay * step)
