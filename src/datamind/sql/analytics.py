"""SQLite analytics with GROUP BY and window RANK."""
from __future__ import annotations
import sqlite3
from pathlib import Path
import pandas as pd


def connect(db_path: Path | str) -> sqlite3.Connection:
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    return conn


def load_table(conn: sqlite3.Connection, df: pd.DataFrame, table: str = "dataset") -> None:
    df.to_sql(table, conn, if_exists="replace", index=False)


def group_by_avg(conn: sqlite3.Connection, table: str, group_col: str, value_col: str) -> pd.DataFrame:
    sql = (
        f"SELECT {group_col} AS grp, AVG({value_col}) AS avg_value, COUNT(*) AS n "
        f"FROM {table} GROUP BY {group_col} ORDER BY grp"
    )
    return pd.read_sql_query(sql, conn)


def rank_by_value(conn: sqlite3.Connection, table: str, value_col: str, limit: int = 10) -> pd.DataFrame:
    """Window RANK over value_col descending."""
    sql = f"""
    SELECT * FROM (
        SELECT *, RANK() OVER (ORDER BY {value_col} DESC) AS rnk
        FROM {table}
    ) t
    WHERE rnk <= {{limit}}
    ORDER BY rnk
    """.replace("{limit}", str(int(limit)))
    return pd.read_sql_query(sql, conn)
