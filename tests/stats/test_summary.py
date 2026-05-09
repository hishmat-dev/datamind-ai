from datamind.data.generate import generate_housing
from datamind.stats.summary import correlation_matrix, summarize_numeric

def test_summary():
    df = generate_housing(60, seed=5)
    summaries = summarize_numeric(df)
    assert len(summaries) >= 5
    assert summaries[0].count > 0
    corr = correlation_matrix(df)
    assert "price" in corr.columns
