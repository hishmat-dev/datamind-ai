from pathlib import Path
from datamind.data.loader import load_dataset
from datamind.sql.analytics import connect, group_by_avg, load_table, rank_by_value

def test_group_and_rank(tmp_path: Path):
    conn = connect(tmp_path / "a.db")
    df = load_dataset("housing", n_samples=40, seed=0).frame
    load_table(conn, df, "dataset")
    g = group_by_avg(conn, "dataset", "rooms", "price")
    assert len(g) >= 1
    ranked = rank_by_value(conn, "dataset", "price", limit=5)
    assert len(ranked) <= 5 and "rnk" in ranked.columns
    conn.close()
