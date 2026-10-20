# Model card — synthetic housing price models

## Model details
- **Mean baseline**: predicts training mean
- **Linear GD**: batch gradient descent linear regressor with optional L2

## Intended use
Educational comparison of baselines on synthetic housing-like data.

## Training data
`generate_housing` — synthetic features (rooms, area, age, distance, crime, school).

## Metrics
RMSE, MAE, R² on held-out split (default 20%, seed 42).

## Limitations
Synthetic data; no geographic or legal housing realism; not for lending decisions.
