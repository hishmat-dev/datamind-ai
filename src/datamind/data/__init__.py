"""Data ingestion, validation, and cleaning."""
from datamind.data.clean import drop_duplicates, impute_numeric_median
from datamind.data.generate import generate_housing
from datamind.data.io import ensure_sample_dataset, load_csv, save_processed
from datamind.data.validate import assert_valid, validate_dataframe
