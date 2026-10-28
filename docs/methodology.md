# Methodology

1. Load a dataset bundle and run validation (missing/dup/outlier/leakage).
2. Split train/test with a fixed seed.
3. Fit preprocessing on **train only**, transform train and test.
4. Fit model; compute task-appropriate metrics.
5. Optionally log experiments to SQLite and export JSON via `ExperimentResult`.
