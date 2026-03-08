from pathlib import Path
from datamind.analytics.queries import avg_price_by_rooms, experiment_leaderboard
from datamind.analytics.sql_store import connect, init_schema, load_dataframe, record_experiment
from datamind.data.generate import generate_housing

def test_queries(tmp_path: Path):
    conn = connect(tmp_path / "q.db")
    init_schema(conn)
    load_dataframe(conn, generate_housing(30, seed=9))
    record_experiment(conn, "linear_gd", 1.0, 0.9, 0.7)
    assert len(avg_price_by_rooms(conn)) >= 1
    assert experiment_leaderboard(conn).iloc[0]["model_name"] == "linear_gd"
    conn.close()
