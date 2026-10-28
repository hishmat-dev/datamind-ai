# Architecture

```
app.py / pages/          Streamlit UI
src/datamind/data        loaders + validation
src/datamind/preprocessing  impute → scale → one-hot (train-fit)
src/datamind/models      factory (5 reg + 4 clf)
src/datamind/evaluation  metrics
src/datamind/experiments runner + ExperimentResult
src/datamind/optimization  GD vs OLS lab
src/datamind/explainability  coefficients + permutation
src/datamind/sql         SQLite GROUP BY + RANK
```
