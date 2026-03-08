"""Named SQL analytics queries."""
from __future__ import annotations
import sqlite3
import pandas as pd

def avg_price_by_rooms(conn: sqlite3.Connection) -> pd.DataFrame:
    return pd.read_sql_query(
        "SELECT ROUND(rooms) AS rooms_bin, AVG(price) AS avg_price, COUNT(*) AS n "
        "FROM housing GROUP BY rooms_bin ORDER BY rooms_bin",
        conn,
    )

def experiment_leaderboard(conn: sqlite3.Connection) -> pd.DataFrame:
    return pd.read_sql_query(
        "SELECT model_name, rmse, mae, r2 FROM experiments ORDER BY r2 DESC",
        conn,
    )
