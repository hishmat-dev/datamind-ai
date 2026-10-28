# DataMind AI

**Version:** 0.2.0  
**Python:** 3.11 – 3.14 (including 3.14.x)

DataMind AI is a reproducible data science and machine learning research toolkit.
It focuses on transparent pipelines: synthetic research data, cleaning, statistics,
feature engineering, baseline and gradient-descent models, explainability,
SQLite analytics, and an optional Streamlit dashboard.

## Features

- Four research datasets (housing, diabetes, iris, wine) with fixed-seed generation
- Schema validation and cleaning (imputation, outlier checks, standardization)
- Preprocessing pipeline: impute → scale → one-hot (train-only fit)
- Exploratory statistics and correlation analysis
- Feature engineering (ratios, polynomials, log target)
- 5 regression + 4 classification models (mean, linear GD, ridge, kNN, median; majority, logistic GD, kNN, threshold)
- Evaluation metrics: MAE/RMSE/R²; accuracy/precision/recall/F1/ROC-AUC/confusion matrix
- Experiment runner with `ExperimentResult` metadata
- Ridge / closed-form OLS and educational batch gradient descent
- Coefficient and permutation feature importance
- Residual uncertainty and bootstrap-style metric helpers
- SQLite analytics (GROUP BY, window RANK) and report export
- Streamlit UI: Overview, ML Workbench, Math Lab
- Pytest suite with coverage gate (75%+)

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

## Quick start

### pip + venv (recommended on Python 3.14)

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

# Windows
set PYTHONPATH=src
# macOS/Linux
export PYTHONPATH=src

python -m pytest
streamlit run app.py
python scripts/run_baseline_experiments.py
