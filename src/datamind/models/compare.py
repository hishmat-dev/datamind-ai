"""Compare multiple train results."""
from __future__ import annotations
from datamind.models.pipeline import TrainResult

def rank_by_metric(results: list[TrainResult], metric: str = "rmse", higher_better: bool = False) -> list[TrainResult]:
    return sorted(results, key=lambda r: r.metrics[metric], reverse=higher_better)

def best_model(results: list[TrainResult], metric: str = "r2") -> TrainResult:
    return rank_by_metric(results, metric=metric, higher_better=True)[0]
