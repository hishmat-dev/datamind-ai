from datamind.data.generate import generate_housing
from datamind.stats.plots_data import histogram_bins, top_correlations
from datamind.stats.summary import correlation_matrix

def test_plot_data():
    df = generate_housing(80, seed=3)
    counts, edges = histogram_bins(df["price"], bins=8)
    assert len(counts) == 8
    top = top_correlations(correlation_matrix(df), "price", k=3)
    assert len(top) <= 3
