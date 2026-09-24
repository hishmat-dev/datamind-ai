"""Streamlit dashboard entry (optional UI dependency)."""
from __future__ import annotations

def build_overview_text(n_rows: int, r2: float | None = None) -> str:
    """Pure helper so dashboard text is unit-testable without Streamlit."""
    parts = [f"Dataset rows: {n_rows}"]
    if r2 is not None:
        parts.append(f"Latest model R²: {r2:.3f}")
    return " | ".join(parts)


def run() -> None:
    import streamlit as st
    from datamind.data.generate import generate_housing
    from datamind.features.engineering import add_area_per_room
    from datamind.features.split import train_test_split
    from datamind.models.pipeline import dataframe_to_xy, train_linear_gd

    st.set_page_config(page_title="DataMind AI", layout="wide")
    st.title("DataMind AI")
    st.write("Reproducible housing-price experiments")

    n = st.slider("Samples", 100, 2000, 500, 50)
    df = add_area_per_room(generate_housing(n_samples=n, seed=42))
    st.dataframe(df.head(20))
    st.write(build_overview_text(len(df)))

    if st.button("Train linear model"):
        x_train, x_test, y_train, y_test = train_test_split(df, "price", seed=42)
        # drop non-numeric engineered cols if any
        num_cols = [c for c in x_train.columns if c != "age_band"]
        xtr, ytr = dataframe_to_xy(x_train, y_train, num_cols)
        xte, yte = dataframe_to_xy(x_test, y_test, num_cols)
        # standardize roughly via z-score for GD stability
        mu, sigma = xtr.mean(axis=0), xtr.std(axis=0) + 1e-8
        xtr = (xtr - mu) / sigma
        xte = (xte - mu) / sigma
        result = train_linear_gd(xtr, ytr, xte, yte, lr=0.05, n_iter=400)
        st.json(result.metrics)
        st.write(build_overview_text(len(df), result.metrics["r2"]))


if __name__ == "__main__":
    run()
