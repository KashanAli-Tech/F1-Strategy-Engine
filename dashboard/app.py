
import streamlit as st

from pages import (
    home,
    strategy_optimiser,
    monte_carlo,
    tyre_analysis,
    calibration,
    backtesting,
    strategy_input,
)

st.set_page_config(
    page_title="F1 Probabilistic Strategy Optimiser",
    page_icon="🏎️",
    layout="wide",
)


def main():

    st.sidebar.title("F1 Strategy Engine")

    pages = [
        "Home",
        "Strategy Input",
        "Strategy Optimiser",
        "Monte Carlo Results",
        "Backtester",
        "Tyre Degradation",
        "Track Calibration"
    ]

    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

    selected_page = st.sidebar.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state["current_page"])
    )

    st.session_state["current_page"] = selected_page

    page = st.session_state["current_page"]

    if page == "Home":
        home.show()

    elif page == "Strategy Input":
        strategy_input.show()

    elif page == "Strategy Optimiser":
        strategy_optimiser.show()

    elif page == "Monte Carlo Results":
        monte_carlo.show()

    elif page == "Backtester":
        backtesting.show()

    elif page == "Tyre Degradation":
        tyre_analysis.show()

    elif page == "Track Calibration":
        calibration.show()


if __name__ == "__main__":
    main()
