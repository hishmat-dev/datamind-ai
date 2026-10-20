# DataMind AI — development backlog (120+ tasks)

| ID | Component | Objective | Files | Tests | Commit message |
|----|-----------|-----------|-------|-------|----------------|
| DM-001 | core | config settings | `src/datamind/core/config.py` | tests/core | `feat(core): config settings` |
| DM-002 | core | logging helper | `src/datamind/core/logging.py` | tests/core | `feat(core): logging helper` |
| DM-003 | data | dataset schema | `src/datamind/data/schema.py` | tests/data/test_validate.py | `feat(data): dataset schema` |
| DM-004 | data | synthetic generator | `src/datamind/data/generate.py` | tests/data/test_generate.py | `feat(data): synthetic generator` |
| DM-005 | data | validation layer | `src/datamind/data/validate.py` | tests/data/test_validate.py | `feat(data): validation layer` |
| DM-006 | data | CSV IO helpers | `src/datamind/data/io.py` | tests/data | `feat(data): CSV IO helpers` |
| DM-007 | data | deduplicate rows | `src/datamind/data/clean.py` | tests/data/test_clean.py | `feat(data): deduplicate rows` |
| DM-008 | data | median imputation | `src/datamind/data/clean.py` | tests/data/test_clean.py | `feat(data): median imputation` |
| DM-009 | data | IQR outlier clip | `src/datamind/data/clean.py` | tests/data/test_clean.py | `feat(data): IQR outlier clip` |
| DM-010 | data | standardize columns | `src/datamind/data/clean.py` | tests/data/test_clean.py | `feat(data): standardize columns` |
| DM-011 | stats | numeric summary | `src/datamind/stats/summary.py` | tests/stats/test_summary.py | `feat(stats): numeric summary` |
| DM-012 | stats | correlation matrix | `src/datamind/stats/summary.py` | tests/stats/test_summary.py | `feat(stats): correlation matrix` |
| DM-013 | stats | IQR outlier mask | `src/datamind/stats/outliers.py` | tests/stats/test_outliers.py | `feat(stats): IQR outlier mask` |
| DM-014 | stats | z-score outliers | `src/datamind/stats/outliers.py` | tests/stats/test_outliers.py | `feat(stats): z-score outliers` |
| DM-015 | features | area per room | `src/datamind/features/engineering.py` | tests/features/test_engineering.py | `feat(features): area per room` |
| DM-016 | features | age band feature | `src/datamind/features/engineering.py` | tests/features/test_engineering.py | `feat(features): age band feature` |
| DM-017 | features | log price target | `src/datamind/features/engineering.py` | tests/features/test_engineering.py | `feat(features): log price target` |
| DM-018 | features | polynomial terms | `src/datamind/features/engineering.py` | tests/features/test_engineering.py | `feat(features): polynomial terms` |
| DM-019 | features | train test split | `src/datamind/features/split.py` | tests/features/test_split.py | `feat(features): train test split` |
| DM-020 | models | MSE metric | `src/datamind/models/metrics.py` | tests/models/test_metrics.py | `feat(models): MSE metric` |
| DM-021 | models | RMSE metric | `src/datamind/models/metrics.py` | tests/models/test_metrics.py | `feat(models): RMSE metric` |
| DM-022 | models | MAE metric | `src/datamind/models/metrics.py` | tests/models/test_metrics.py | `feat(models): MAE metric` |
| DM-023 | models | R2 metric | `src/datamind/models/metrics.py` | tests/models/test_metrics.py | `feat(models): R2 metric` |
| DM-024 | models | mean baseline | `src/datamind/models/baselines.py` | tests/models/test_baselines.py | `feat(models): mean baseline` |
| DM-025 | models | linear GD fit | `src/datamind/models/baselines.py` | tests/models/test_baselines.py | `feat(models): linear GD fit` |
| DM-026 | models | linear GD predict | `src/datamind/models/baselines.py` | tests/models/test_baselines.py | `feat(models): linear GD predict` |
| DM-027 | models | training pipeline | `src/datamind/models/pipeline.py` | tests/models/test_pipeline.py | `feat(models): training pipeline` |
| DM-028 | models | model persistence | `src/datamind/models/persist.py` | tests/models/test_persist.py | `feat(models): model persistence` |
| DM-029 | math | quadratic loss | `src/datamind/math/gradient_descent.py` | tests/math/test_gradient_descent.py | `feat(math): quadratic loss` |
| DM-030 | math | GD optimizer | `src/datamind/math/gradient_descent.py` | tests/math/test_gradient_descent.py | `feat(math): GD optimizer` |
| DM-031 | math | numerical gradient | `src/datamind/math/gradient_descent.py` | tests/math/test_gradient_descent.py | `feat(math): numerical gradient` |
| DM-032 | math | L2 penalty | `src/datamind/math/regularization.py` | tests/math/test_regularization.py | `feat(math): L2 penalty` |
| DM-033 | math | L1 penalty | `src/datamind/math/regularization.py` | tests/math/test_regularization.py | `feat(math): L1 penalty` |
| DM-034 | math | ridge closed form | `src/datamind/math/regularization.py` | tests/math/test_regularization.py | `feat(math): ridge closed form` |
| DM-035 | explain | coefficient importance | `src/datamind/explain/importance.py` | tests/explain/test_importance.py | `feat(explain): coefficient importance` |
| DM-036 | explain | permutation importance | `src/datamind/explain/importance.py` | tests/explain/test_importance.py | `feat(explain): permutation importance` |
| DM-037 | explain | residual std | `src/datamind/explain/uncertainty.py` | tests/explain/test_uncertainty.py | `feat(explain): residual std` |
| DM-038 | explain | prediction intervals | `src/datamind/explain/uncertainty.py` | tests/explain/test_uncertainty.py | `feat(explain): prediction intervals` |
| DM-039 | explain | bootstrap metrics | `src/datamind/explain/uncertainty.py` | tests/explain/test_uncertainty.py | `feat(explain): bootstrap metrics` |
| DM-040 | analytics | sqlite schema | `src/datamind/analytics/sql_store.py` | tests/analytics/test_sql_store.py | `feat(analytics): sqlite schema` |
| DM-041 | analytics | load dataframe SQL | `src/datamind/analytics/sql_store.py` | tests/analytics/test_sql_store.py | `feat(analytics): load dataframe SQL` |
| DM-042 | analytics | record experiment | `src/datamind/analytics/sql_store.py` | tests/analytics/test_sql_store.py | `feat(analytics): record experiment` |
| DM-043 | analytics | metrics report | `src/datamind/analytics/reports.py` | tests/analytics/test_reports.py | `feat(analytics): metrics report` |
| DM-044 | app | dashboard overview text | `src/datamind/app/dashboard.py` | tests/app/test_dashboard_text.py | `feat(app): dashboard overview text` |
| DM-045 | app | streamlit train button path | `src/datamind/app/dashboard.py` | tests/app/test_dashboard_text.py | `feat(app): streamlit train button path` |
| DM-046 | integration | end-to-end pipeline | `tests/integration/test_end_to_end.py` | tests/integration/test_end_to_end.py | `feat(integration): end-to-end pipeline` |
| DM-047 | ci | github actions workflow | `.github/workflows/ci.yml` | CI | `feat(ci): github actions workflow` |
| DM-048 | docs | README quickstart | `README.md` | docs | `feat(docs): README quickstart` |
| DM-049 | docs | model card | `docs/model_card.md` | docs | `feat(docs): model card` |
| DM-050 | docs | design notes | `docs/design.md` | docs | `feat(docs): design notes` |
| DM-051 | stats | add rooms validation bounds | src/datamind/ | tests/ | `feat(stats): add rooms validation bounds` |
| DM-052 | features | document schema license | src/datamind/ | tests/ | `feat(features): document schema license` |
| DM-053 | models | seed configuration flag | src/datamind/ | tests/ | `feat(models): seed configuration flag` |
| DM-054 | math | missing value report helper | src/datamind/ | tests/ | `feat(math): missing value report helper` |
| DM-055 | explain | clip price outliers | src/datamind/ | tests/ | `feat(explain): clip price outliers` |
| DM-056 | analytics | export correlation CSV | src/datamind/ | tests/ | `feat(analytics): export correlation CSV` |
| DM-057 | app | feature interaction rooms*area | src/datamind/ | tests/ | `feat(app): feature interaction rooms*area` |
| DM-058 | ci | stratify split option | src/datamind/ | tests/ | `feat(ci): stratify split option` |
| DM-059 | docs | classification threshold helper | src/datamind/ | tests/ | `feat(docs): classification threshold helper` |
| DM-060 | data | confusion matrix stub | src/datamind/ | tests/ | `feat(data): confusion matrix stub` |
| DM-061 | stats | accuracy metric | src/datamind/ | tests/ | `feat(stats): accuracy metric` |
| DM-062 | features | precision metric stub | src/datamind/ | tests/ | `feat(features): precision metric stub` |
| DM-063 | models | recall metric stub | src/datamind/ | tests/ | `feat(models): recall metric stub` |
| DM-064 | math | f1 metric stub | src/datamind/ | tests/ | `feat(math): f1 metric stub` |
| DM-065 | explain | learning rate schedule | src/datamind/ | tests/ | `feat(explain): learning rate schedule` |
| DM-066 | analytics | early stopping GD | src/datamind/ | tests/ | `feat(analytics): early stopping GD` |
| DM-067 | app | mini-batch GD option | src/datamind/ | tests/ | `feat(app): mini-batch GD option` |
| DM-068 | ci | weight initialization zeros | src/datamind/ | tests/ | `feat(ci): weight initialization zeros` |
| DM-069 | docs | weight initialization xavier stub | src/datamind/ | tests/ | `feat(docs): weight initialization xavier stub` |
| DM-070 | data | compare baseline vs linear | src/datamind/ | tests/ | `feat(data): compare baseline vs linear` |
| DM-071 | stats | hyperparam grid lr | src/datamind/ | tests/ | `feat(stats): hyperparam grid lr` |
| DM-072 | features | hyperparam grid l2 | src/datamind/ | tests/ | `feat(features): hyperparam grid l2` |
| DM-073 | models | save metrics json | src/datamind/ | tests/ | `feat(models): save metrics json` |
| DM-074 | math | load metrics json | src/datamind/ | tests/ | `feat(math): load metrics json` |
| DM-075 | explain | plot loss history stub | src/datamind/ | tests/ | `feat(explain): plot loss history stub` |
| DM-076 | analytics | math docs for GD | src/datamind/ | tests/ | `feat(analytics): math docs for GD` |
| DM-077 | app | verify grad check tolerance | src/datamind/ | tests/ | `feat(app): verify grad check tolerance` |
| DM-078 | ci | ridge alpha sweep | src/datamind/ | tests/ | `feat(ci): ridge alpha sweep` |
| DM-079 | docs | elastic net stub | src/datamind/ | tests/ | `feat(docs): elastic net stub` |
| DM-080 | data | feature ranking table | src/datamind/ | tests/ | `feat(data): feature ranking table` |
| DM-081 | stats | top-k importance filter | src/datamind/ | tests/ | `feat(stats): top-k importance filter` |
| DM-082 | features | bootstrap seed control | src/datamind/ | tests/ | `feat(features): bootstrap seed control` |
| DM-083 | models | interval coverage test | src/datamind/ | tests/ | `feat(models): interval coverage test` |
| DM-084 | math | SQL avg price by rooms | src/datamind/ | tests/ | `feat(math): SQL avg price by rooms` |
| DM-085 | explain | SQL experiment leaderboard | src/datamind/ | tests/ | `feat(explain): SQL experiment leaderboard` |
| DM-086 | analytics | markdown report footer | src/datamind/ | tests/ | `feat(analytics): markdown report footer` |
| DM-087 | app | dashboard sample slider | src/datamind/ | tests/ | `feat(app): dashboard sample slider` |
| DM-088 | ci | dashboard metrics panel | src/datamind/ | tests/ | `feat(ci): dashboard metrics panel` |
| DM-089 | docs | CI python 3.11 | src/datamind/ | tests/ | `feat(docs): CI python 3.11` |
| DM-090 | data | CI python 3.12 | src/datamind/ | tests/ | `feat(data): CI python 3.12` |
| DM-091 | stats | Makefile test target | src/datamind/ | tests/ | `feat(stats): Makefile test target` |
| DM-092 | features | Makefile lint target | src/datamind/ | tests/ | `feat(features): Makefile lint target` |
| DM-093 | models | coverage fail under 80 | src/datamind/ | tests/ | `feat(models): coverage fail under 80` |
| DM-094 | math | ruff config | src/datamind/ | tests/ | `feat(math): ruff config` |
| DM-095 | explain | mypy config | src/datamind/ | tests/ | `feat(explain): mypy config` |
| DM-096 | analytics | env example file | src/datamind/ | tests/ | `feat(analytics): env example file` |
| DM-097 | app | gitignore artifacts | src/datamind/ | tests/ | `feat(app): gitignore artifacts` |
| DM-098 | ci | license MIT | src/datamind/ | tests/ | `feat(ci): license MIT` |
| DM-099 | docs | contributing guide | src/datamind/ | tests/ | `feat(docs): contributing guide` |
| DM-100 | data | changelog init | src/datamind/ | tests/ | `feat(data): changelog init` |
| DM-101 | stats | release notes 0.1.0 | src/datamind/ | tests/ | `feat(stats): release notes 0.1.0` |
| DM-102 | features | data raw directory | src/datamind/ | tests/ | `feat(features): data raw directory` |
| DM-103 | models | data processed directory | src/datamind/ | tests/ | `feat(models): data processed directory` |
| DM-104 | math | scripts train entry | src/datamind/ | tests/ | `feat(math): scripts train entry` |
| DM-105 | explain | scripts evaluate entry | src/datamind/ | tests/ | `feat(explain): scripts evaluate entry` |
| DM-106 | analytics | reproducibility checklist | src/datamind/ | tests/ | `feat(analytics): reproducibility checklist` |
| DM-107 | app | seed audit test | src/datamind/ | tests/ | `feat(app): seed audit test` |
| DM-108 | ci | null age imputation test | src/datamind/ | tests/ | `feat(ci): null age imputation test` |
| DM-109 | docs | duplicate row test | src/datamind/ | tests/ | `feat(docs): duplicate row test` |
| DM-110 | data | schema extra column test | src/datamind/ | tests/ | `feat(data): schema extra column test` |
| DM-111 | stats | empty frame guard | src/datamind/ | tests/ | `feat(stats): empty frame guard` |
| DM-112 | features | single row split guard | src/datamind/ | tests/ | `feat(features): single row split guard` |
| DM-113 | models | constant target r2 guard | src/datamind/ | tests/ | `feat(models): constant target r2 guard` |
| DM-114 | math | zero std standardize guard | src/datamind/ | tests/ | `feat(math): zero std standardize guard` |
| DM-115 | explain | permutation seed stability | src/datamind/ | tests/ | `feat(explain): permutation seed stability` |
| DM-116 | analytics | SQL inject-safe params | src/datamind/ | tests/ | `feat(analytics): SQL inject-safe params` |
| DM-117 | app | experiment notes field | src/datamind/ | tests/ | `feat(app): experiment notes field` |
| DM-118 | ci | report extra lines | src/datamind/ | tests/ | `feat(ci): report extra lines` |
| DM-119 | docs | dashboard without streamlit import in tests | src/datamind/ | tests/ | `feat(docs): dashboard without streamlit import in tests` |
| DM-120 | data | integration explains weights | src/datamind/ | tests/ | `feat(data): integration explains weights` |
| DM-121 | stats | integration records SQL | src/datamind/ | tests/ | `feat(stats): integration records SQL` |
| DM-122 | features | docs roadmap month1 | src/datamind/ | tests/ | `feat(features): docs roadmap month1` |
| DM-123 | models | docs roadmap month2 | src/datamind/ | tests/ | `feat(models): docs roadmap month2` |
| DM-124 | math | docs roadmap month3 | src/datamind/ | tests/ | `feat(math): docs roadmap month3` |
| DM-125 | explain | docs backlog index | src/datamind/ | tests/ | `feat(explain): docs backlog index` |
| DM-126 | analytics | fix type hints models | src/datamind/ | tests/ | `feat(analytics): fix type hints models` |
| DM-127 | app | fix type hints data | src/datamind/ | tests/ | `feat(app): fix type hints data` |
| DM-128 | ci | refactor pipeline xy helper | src/datamind/ | tests/ | `feat(ci): refactor pipeline xy helper` |
| DM-129 | docs | add __version__ | src/datamind/ | tests/ | `feat(docs): add __version__` |
| DM-130 | data | export public API data | src/datamind/ | tests/ | `feat(data): export public API data` |
| DM-131 | stats | export public API models | src/datamind/ | tests/ | `feat(stats): export public API models` |
