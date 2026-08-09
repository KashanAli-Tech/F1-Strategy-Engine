import streamlit as st

from pages import home, strategy_optimiser, monte_carlo, tyre_analysis, calibration, backtesting, strategy_input
from utils.race_config import (get_races, get_available_years, get_drivers)

st.set_page_config(page_title="F1 Probabilistic Strategy Optimiser", page_icon="🏎️", layout="wide")

def main():
    st.sidebar.title("F1 Strategy Engine")

    with st.sidebar:
            st.header("Race Configuration")

            selected_year = st.selectbox("Select Season", [2022, 2023, 2024])
            races = get_races(selected_year)
            selected_race = st.selectbox("Select Grand Prix", races)

            available_years = get_available_years(selected_race)
            selected_years = st.multiselect("Calibration Years", available_years, default=available_years)

            drivers = get_drivers(selected_year, selected_race)
            selected_driver_name = st.selectbox("Driver", list(drivers.keys()))
            selected_driver = drivers[selected_driver_name]

            st.session_state["race_name"] = selected_race
            st.session_state["years"] = selected_years
            st.session_state["driver_code"] = selected_driver
    
            simulations = st.slider("Monte Carlo Simulations", 100, 5000, 1000, step=100)
            st.divider()
            st.write("Selected:")
            st.write(selected_race)   
            st.write(selected_driver_name)
    

    page = st.sidebar.radio("Navigation",
        ["Home",
         "Strategy Input",
        "Strategy Optimiser",
        "Monte Carlo Results",
        "Backtester",
        "Tyre Degradation",
        "Track Calibration"])

    
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