import streamlit as st

from pages import home, strategy_optimiser, monte_carlo, validation, tyre_analysis, calibration

st.set_page_config(page_title="F1 Probabilistic Strategy Optimiser", page_icon="🏎️", layout="wide")

def main():
    st.sidebar.title("F1 Strategy Engine")
    page = st.sidebar.radio("Navigation",
        ["Home",
        "Strategy Optimiser",
        "Monte Carlo Results",
        "Historical Validation",
        "Tyre Degradation",
        "Track Calibration"])

    if page == "Home":
        home.show()

    elif page == "Strategy Optimiser":
        strategy_optimiser.show()

    elif page == "Monte Carlo Results":
        monte_carlo.show()

    elif page == "Historical Validation":
        validation.show()

    elif page == "Tyre Degradation":
        tyre_analysis.show()

    elif page == "Track Calibration":
        calibration.show()

if __name__ == "__main__":
    main()