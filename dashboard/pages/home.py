import streamlit as st


def show():

    st.title("🏎️ F1 Probabilistic Strategy Optimiser")
    st.subheader("Welcome to the Strategy Engine")
    st.write("""This dashboard provides an interactive view of a probabilistic Formula 1 race strategy optimisation system.
        The engine combines historical race data, statistical modelling, Monte Carlo simulation, and optimisation techniques to evaluate 
        different race strategies under uncertainty.""")
    st.divider()
    st.subheader("Current Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Data Source", "FastF1")

    with col2:
        st.metric("Simulation Method", "Monte Carlo")

    st.divider()
    st.subheader("Model Pipeline")
    st.code("""
Historical Race Data
        ↓
Lap Extraction
        ↓
Parameter Estimation
        ↓
Tyre Degradation Modelling
        ↓
Monte Carlo Simulation
        ↓
Risk Analysis
        ↓
Strategy Optimisation
        ↓
Historical Validation""")