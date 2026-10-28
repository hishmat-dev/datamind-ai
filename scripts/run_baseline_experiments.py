"""Run baseline experiments across datasets and print metrics."""
from __future__ import annotations
from datamind.data.loader import list_datasets, load_dataset
from datamind.experiments.runner import run_experiment
from datamind.models.factory import list_models


def main() -> None:
    for name in list_datasets():
        task = load_dataset(name).task
        for model in list_models(task)[:3]:
            result = run_experiment(dataset=name, model=model, seed=42)
            print(name, model, result.metrics)


if __name__ == "__main__":
    main()
