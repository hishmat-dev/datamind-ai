from datamind.experiments.runner import run_experiment

def test_run_regression():
    r = run_experiment(dataset="housing", model="mean", seed=1)
    assert r.task == "regression" and "rmse" in r.metrics

def test_run_classification():
    r = run_experiment(dataset="iris", model="majority", seed=1)
    assert r.task == "classification" and "accuracy" in r.metrics
