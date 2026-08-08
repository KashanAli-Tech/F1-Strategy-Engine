import streamlit as st
import pandas as pd

from utils.engine_runner import run_strategy_engine
from src.data.parameter_estimator import ParameterEstimator


def show():
    st.title("Track Calibration")

    st.write("""Before race strategy optimisation, the simulation environment is calibrated using historical Formula 1 race data.
    This ensures the race simulator is parameterised using observed performance rather than fixed assumptions.""")
    st.divider()

    engine = run_strategy_engine(st.session_state["race_name"], st.session_state["years"], st.session_state["driver_code"])

    track = engine["track"]
    laps = engine["laps"]

    estimator = ParameterEstimator()

    average_lap = estimator.estimate_average_pace(laps)
    fastest_lap = estimator.estimate_fastest_lap(laps)
    stints = estimator.estimate_stint_lengths(laps)

    st.subheader("Calibrated Track Parameters")
    col1, col2 = st.columns(2)

    with col1:

        st.metric("Track", track.name)
        st.metric("Base Lap Time", f"{track.base_lap_time:.3f}s")
        st.metric("Fuel Effect", f"{track.fuel_effect_per_lap:.3f}s/lap")

    with col2:

        st.metric("Tyre Wear Multiplier", f"{track.tyre_wear_multiplier:.3f}")
        st.metric("Track Evolution", f"{track.track_evolution_rate:.3f}")
        st.metric("Number of Laps", track.number_of_laps)

    st.divider()

    st.subheader("Historical Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric("Average Lap Time", f"{average_lap:.3f}s")

    with col2:

        st.metric("Fastest Lap", f"{fastest_lap:.3f}s")

    with col3:

        st.metric("Average Stint Length", f"{sum(stints) / len(stints):.1f} laps")

    st.divider()

    st.subheader("Estimated Stint Lengths")
    stint_df = pd.DataFrame({"Stint Number": range(1, len(stints) + 1),"Length (laps)": stints})

    st.dataframe(stint_df, use_container_width=True)
    st.divider()

    st.subheader("Calibration Summary")

    st.info(
        f"""Historical race data from the British Grand Prix ({', '.join(map(str, sorted(laps['Year'].unique())))}) was used to calibrate the simulation environment.
        The calibrated parameters shown above are subsequently used by the Monte Carlo simulator and strategy optimisation engine.""")