# DataMind AI

**DataMind AI** is a reproducible data science and machine learning research toolkit.
It focuses on transparent pipelines: synthetic research data, cleaning, statistics,
feature engineering, baseline and gradient-descent models, explainability,
SQLite analytics, and an optional Streamlit dashboard.

## Features

- Synthetic housing dataset with fixed-seed generation
- Schema validation and cleaning (imputation, outlier clipping, standardization)
- Exploratory statistics and correlation analysis
- Feature engineering (ratios, polynomials, log target)
- Mean baseline and linear regression via batch gradient descent
- Ridge closed-form solver and educational GD utilities
- Coefficient and permutation feature importance
- Residual uncertainty and bootstrap metric intervals
- SQLite experiment logging and SQL queries
- Streamlit dashboard for interactive exploration
- Pytest suite with coverage gate (80%+)

## Quick start

```bash
poetry install --no-interaction --with dev
make test
make data
poetry run streamlit run src/datamind/app/dashboard.py  # optional UI extra
```

## Project layout

```
src/datamind/
  data/        ingestion, schema, cleaning
  stats/       summaries and outlier analysis
  features/    engineering and splits
  models/      baselines, metrics, persistence
  math/        gradient descent, regularization
  explain/     importance and uncertainty
  analytics/   SQLite + reports
  app/         Streamlit dashboard
tests/         unit and integration tests
docs/          design notes, model card, backlog
```

## Research scope

DataMind AI is an **educational / research engineering** codebase. The default
dataset is synthetic. Do not treat model outputs as production valuations.

## License

MIT


## Module checklist

| Module | Status |
|--------|--------|
| Data load + validation (4 datasets) | yes |
| Preprocessing (impute → scale → one-hot) | yes |
| Models (5 regression + 4 classification) | yes |
| Evaluation (reg + clf metrics) | yes |
| Experiment runner | yes |
| Gradient descent lab vs OLS | yes |
| Explainability | yes |
| SQL analytics (GROUP BY, RANK) | yes |
| Streamlit (Overview + Workbench + Math Lab) | yes |
| Tests + CI (`tests.yml`) | yes |

```bash
poetry run streamlit run app.py
poetry run python scripts/run_baseline_experiments.py
```
