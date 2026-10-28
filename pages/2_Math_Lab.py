"""Math Lab — batch GD vs closed-form OLS."""
from __future__ import annotations
import numpy as np
import streamlit as st
from datamind.data.loader import load_dataset
from datamind.optimization.ols import compare_ols_to_gd
from datamind.preprocessing.pipeline import PreprocessPipeline

st.set_page_config(page_title="Math Lab", layout="wide")
st.title("Math Lab — Gradient Descent vs OLS")

bundle = load_dataset("housing", n_samples=300, seed=42)
x = bundle.frame[list(bundle.feature_cols)]
y = bundle.frame[bundle.target].to_numpy(dtype=float)
pipe = PreprocessPipeline().fit(x)
x_arr = pipe.transform(x).to_numpy(dtype=float)
# drop nan rows
mask = np.isfinite(x_arr).all(axis=1) & np.isfinite(y)
x_arr, y = x_arr[mask], y[mask]

lr = st.slider("Learning rate", 0.001, 0.2, 0.05)
n_iter = st.slider("Iterations", 50, 2000, 500, 50)

if st.button("Compare OLS vs Batch GD"):
    stats = compare_ols_to_gd(x_arr, y, lr=lr, n_iter=n_iter)
    st.json(stats)
