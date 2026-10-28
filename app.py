"""DataMind AI — Streamlit overview entrypoint."""
from __future__ import annotations

def main() -> None:
    import streamlit as st
    from datamind.data.loader import list_datasets, load_dataset
    from datamind.data.validator import validate_dataset

    st.set_page_config(page_title="DataMind AI", layout="wide")
    st.title("DataMind AI")
    st.write(
        "Reproducible data science toolkit: datasets, preprocessing, models, "
        "evaluation, gradient-descent lab, explainability, and SQL analytics."
    )
    st.subheader("Datasets")
    for name in list_datasets():
        bundle = load_dataset(name)
        report = validate_dataset(bundle.frame, bundle.target, list(bundle.feature_cols))
        st.markdown(
            f"**{name}** — task=`{bundle.task}`, rows={len(bundle.frame)}, "
            f"target=`{bundle.target}`, validation_ok={report.ok}"
        )
        st.caption(bundle.license_note)
    st.info("Use the sidebar pages: **ML Workbench** and **Math Lab**.")


if __name__ == "__main__":
    main()
