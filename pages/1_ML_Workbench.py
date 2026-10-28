"""ML Workbench — run experiments interactively."""
from __future__ import annotations
import streamlit as st
from datamind.data.loader import list_datasets, load_dataset
from datamind.experiments.runner import run_experiment
from datamind.models.factory import list_models

st.set_page_config(page_title="ML Workbench", layout="wide")
st.title("ML Workbench")

dataset = st.selectbox("Dataset", list_datasets())
bundle = load_dataset(dataset)
models = list_models(bundle.task)
model = st.selectbox("Model", models)
seed = st.number_input("Seed", min_value=0, value=42, step=1)

if st.button("Run experiment"):
    result = run_experiment(dataset=dataset, model=model, seed=int(seed))
    st.json(result.metrics)
    st.write(
        f"task={result.task} train={result.n_train} test={result.n_test} "
        f"validation_ok={result.validation_ok}"
    )
