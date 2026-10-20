# Design notes

## Principles
1. Reproducibility via fixed seeds
2. Pure functions where practical for unit testing
3. Minimal core dependencies (numpy, pandas); optional Streamlit UI
4. Explicit schemas for dataset contracts

## Gradient descent
Educational implementation prioritizes clarity over speed. Features should be
standardized before training for stable step sizes.
