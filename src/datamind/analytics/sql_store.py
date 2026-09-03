"""SQLite analytics for experiment and dataset queries."""
from __future__ import annotations
import sqlite3
from pathlib import Path
import pandas as pd


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS housing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rooms REAL,
            area_sqm REAL,
            age_years REAL,
            distance_km REAL,
            crime_index REAL,
            school_score REAL,
            price REAL
        );
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            rmse REAL,
            mae REAL,
            r2 REAL,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()


def load_dataframe(conn: sqlite3.Connection, df: pd.DataFrame, table: str = "housing") -> int:
    df.to_sql(table, conn, if_exists="replace", index=False)
    return len(df)


def query_df(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> pd.DataFrame:
    return pd.read_sql_query(sql, conn, params=params)


def record_experiment(
    conn: sqlite3.Connection,
    model_name: str,
    rmse: float,
    mae: float,
    r2: float,
    notes: str = "",
) -> None:
    conn.execute(
        "INSERT INTO experiments (model_name, rmse, mae, r2, notes) VALUES (?, ?, ?, ?, ?)",
        (model_name, rmse, mae, r2, notes),
    )
    conn.commit()
