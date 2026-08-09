
import streamlit as st

from src.data.fastf1_loader import FastF1Loader

loader = FastF1Loader()


def show():

    st.title("Strategy Control Centre")
    st.write("""Welcome, strategist.
        Configure the race, driver and strategy parameters before running the probabilistic strategy engine.""")
    st.divider()

    st.header("Race Selection")
    with st.spinner("Loading available Grand Prix..."):
        current_year = 2026
        races = loader.get_grand_prix(current_year)

    if not races:
        st.error("Unable to load the current F1 calendar.")
        return

    selected_race = st.selectbox("Grand Prix", races)
    st.divider()

    st.header("Season")
    with st.spinner(f"Finding available seasons for the {selected_race}..."):
        available_years = loader.get_available_years(selected_race)

    if not available_years:
        st.error(f"No historical data was found for {selected_race}.")
        return

    selected_year = st.selectbox("Season", sorted(available_years, reverse=True))
    st.divider()


    st.header("Driver")

    with st.spinner(f"Loading drivers from the {selected_race} {selected_year}..."):
        drivers = loader.get_drivers(selected_year, selected_race)

    if not drivers:
        st.error("No drivers were found for this race.")
        return

    selected_driver = st.selectbox("Driver", drivers)
    st.divider()

    st.header("Driver Parameters")
    col1, col2 = st.columns(2)

    with col1:

        aggressiveness = st.slider("Driving Aggressiveness",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help=("Controls how aggressively the driver is assumed "
                "to approach tyre usage and race pace."))

    with col2:

        tyre_management = st.slider("Tyre Management",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help=("Controls the assumed ability to preserve tyre "
                "performance during a stint."))

    consistency = st.slider("Driver Consistency",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05)
    st.divider()

    st.header("Strategy Parameters")

    preferred_compounds = st.multiselect("Available Compounds",
        ["Soft", "Medium", "Hard"],
        default=["Soft", "Medium", "Hard"])

    risk_tolerance = st.slider("Strategy Risk Tolerance",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.1)
    st.divider()

    st.header("Race Conditions")

    weather_mode = st.selectbox("Weather Scenario",
        ["Automatic",
            "Dry",
            "Light Rain",
            "Heavy Rain"])
    
    st.divider()

    st.header("Race Configuration")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Grand Prix", selected_race)

    with col2:
        st.metric("Season", selected_year)

    with col3:
        st.metric("Driver", selected_driver)

    st.divider()

    if st.button("Run Strategy Analysis",
        type="primary",
        use_container_width=True):

        if not preferred_compounds:
            st.error("Select at least one tyre compound.")
            return

        st.session_state["race_name"] = selected_race
        st.session_state["year"] = selected_year
        st.session_state["driver"] = selected_driver

        st.session_state["aggressiveness"] = aggressiveness
        st.session_state["consistency"] = consistency
        st.session_state["tyre_management"] = tyre_management

        st.session_state["preferred_compounds"] = (preferred_compounds)

        st.session_state["risk_tolerance"] = risk_tolerance
        st.session_state["weather_mode"] = weather_mode

        st.session_state["run_analysis"] = True

        st.success(f"Configuration ready: "
            f"{selected_driver} — "
            f"{selected_race} {selected_year}")

        st.info("Your race configuration has been saved. "
            "The strategy engine can now use these parameters.")
