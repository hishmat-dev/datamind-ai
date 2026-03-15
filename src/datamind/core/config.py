"""Project configuration and paths."""
from __future__ import annotations
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DATAMIND_", env_file=".env", extra="ignore")
    project_name: str = "datamind-ai"
    data_raw_dir: Path = Field(default=ROOT / "data" / "raw")
    data_processed_dir: Path = Field(default=ROOT / "data" / "processed")
    models_dir: Path = Field(default=ROOT / "artifacts" / "models")
    reports_dir: Path = Field(default=ROOT / "artifacts" / "reports")
    random_seed: int = 42
    test_size: float = 0.2
    sqlite_path: Path = Field(default=ROOT / "data" / "processed" / "datamind.db")


def get_settings() -> Settings:
    return Settings()
