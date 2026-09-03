from pathlib import Path
from datamind.analytics.sql_store import connect, init_schema, load_dataframe, query_df, record_experiment
from datamind.data.generate import generate_housing

def test_sql_roundtrip(tmp_path: Path):
    conn = connect(tmp_path / "t.db")
    init_schema(conn)
    df = generate_housing(20, seed=11)
    n = load_dataframe(conn, df)
    assert n == 20
    out = query_df(conn, "SELECT COUNT(*) AS c FROM housing")
    assert int(out.iloc[0]["c"]) == 20
    record_experiment(conn, "linear_gd", 1.0, 0.8, 0.7, notes="unit")
    exp = query_df(conn, "SELECT model_name FROM experiments")
    assert exp.iloc[0]["model_name"] == "linear_gd"
    conn.close()
