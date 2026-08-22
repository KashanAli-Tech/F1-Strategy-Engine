import streamlit as st
import pandas as pd
import plotly.express as px

from utils.engine_runner import run_strategy_engine
from src.data.parameter_estimator import ParameterEstimator


def show():

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    with open("dashboard/styles/calibration.css", "r", encoding="utf-8") as f:
        st.html(f"<style>{f.read()}</style>")

    with st.spinner("Calibrating track model from historical race data..."):
        engine = run_strategy_engine(st.session_state["race_name"], st.session_state["years"], st.session_state["driver_code"],)

    track = engine["track"]
    laps = engine["laps"]

    estimator = ParameterEstimator()

    average_lap = estimator.estimate_average_pace(laps)
    fastest_lap = estimator.estimate_fastest_lap(laps)

    stint_data = (laps
        .dropna(subset=["Year", "Driver", "Stint", "LapNumber"])
        .groupby(["Year", "Driver", "Stint"])
        .agg(first_lap=("LapNumber", "min"),
            last_lap=("LapNumber", "max"),
            length=("LapNumber", "count"),)
        .reset_index())

    stints = stint_data["length"].tolist()

    average_stint = (sum(stints) / len(stints) if stints else 0)

    seasons = sorted(laps["Year"].dropna().unique())
    season_text = ", ".join(
        str(int(year))
        for year in seasons
    )

    st.html(f"""
    <div class="calibration-header">

        <div class="calibration-kicker">
            <span>●</span>
            TRACK CALIBRATION / HISTORICAL MODEL
        </div>

        <div class="calibration-title">
            Know the<br>
            <span>circuit.</span>
        </div>

        <div class="calibration-description">
            Historical race data is used to parameterise the simulation
            environment before strategy optimisation. The calibrated
            track model becomes the foundation for the Monte Carlo engine.
        </div>

        <div class="race-context">
            CIRCUIT&nbsp;&nbsp;
            <strong>{track.name}</strong>
            &nbsp;&nbsp;/&nbsp;&nbsp;
            DRIVER&nbsp;&nbsp;
            <strong>{st.session_state["driver_code"]}</strong>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            CALIBRATED ENVIRONMENT
        </div>

        <div class="section-title">
            Track parameters
        </div>

        <div class="section-note">
            PARAMETERS CURRENTLY PASSED INTO THE SIMULATION ENVIRONMENT.
        </div>

    </div>
    """)

    st.html(f"""
    <div class="parameter-grid">

        <div class="parameter-card">
            <div class="parameter-label">
                BASE LAP TIME
            </div>

            <div class="parameter-value">
                {track.base_lap_time:.3f}
            </div>

            <div class="parameter-unit">
                SECONDS
            </div>
        </div>

        <div class="parameter-card">
            <div class="parameter-label">
                FUEL EFFECT
            </div>

            <div class="parameter-value">
                {track.fuel_effect_per_lap:.4f}
            </div>

            <div class="parameter-unit">
                SECONDS / LAP
            </div>
        </div>

        <div class="parameter-card">
            <div class="parameter-label">
                TYRE WEAR
            </div>

            <div class="parameter-value">
                {track.tyre_wear_multiplier:.3f}
            </div>

            <div class="parameter-unit">
                MULTIPLIER
            </div>
        </div>

        <div class="parameter-card">
            <div class="parameter-label">
                TRACK EVOLUTION
            </div>

            <div class="parameter-value">
                {track.track_evolution_rate:.4f}
            </div>

            <div class="parameter-unit">
                MODEL RATE
            </div>
        </div>

        <div class="parameter-card">
            <div class="parameter-label">
                RACE DISTANCE
            </div>

            <div class="parameter-value">
                {track.number_of_laps}
            </div>

            <div class="parameter-unit">
                LAPS
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            HISTORICAL OBSERVATIONS
        </div>

        <div class="section-title">
            What the data says
        </div>

    </div>
    """)

    st.html(f"""
    <div class="historical-grid">

        <div class="historical-card">
            <div class="historical-label">
                AVERAGE LAP
            </div>

            <div class="historical-value">
                {average_lap:.3f}s
            </div>

            <div class="historical-description">
                Mean observed lap pace
            </div>
        </div>

        <div class="historical-card">
            <div class="historical-label">
                FASTEST LAP
            </div>

            <div class="historical-value">
                {fastest_lap:.3f}s
            </div>

            <div class="historical-description">
                Fastest observed lap
            </div>
        </div>

        <div class="historical-card">
            <div class="historical-label">
                AVERAGE STINT
            </div>

            <div class="historical-value">
                {average_stint:.1f}
            </div>

            <div class="historical-description">
                Laps per historical stint
            </div>
        </div>

        <div class="historical-card">
            <div class="historical-label">
                OBSERVATIONS
            </div>

            <div class="historical-value">
                {len(laps):,}
            </div>

            <div class="historical-description">
                Historical lap records
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            STINT PROFILE
        </div>

        <div class="section-title">
            Historical stint lengths
        </div>

        <div class="section-note">
            OBSERVED STINT LENGTHS FROM THE HISTORICAL DATASET.
        </div>

    </div>
    """)

    stint_df = pd.DataFrame({"Stint Number": range(1, len(stints) + 1), "Length (laps)": stints,})

    if not stint_df.empty:

        chart = px.bar(stint_df, x="Stint Number", y="Length (laps)",)

        chart.update_layout(title="",
            template="plotly_dark",
            showlegend=False,
            paper_bgcolor="#13151A",
            plot_bgcolor="#13151A",
            font=dict(family="JetBrains Mono", color="#8D929B",),
            margin=dict(l=25, r=25, t=25, b=25,),
            xaxis=dict(title="Stint",
                gridcolor="rgba(255,255,255,0.04)",
                zeroline=False,),
            yaxis=dict(title="Laps",
                gridcolor="rgba(255,255,255,0.06)",
                zeroline=False,),)

        chart.update_traces(marker_color="#E10600",
            marker_line_width=0,
            hovertemplate=("Stint %{x}"
                "<br>Length: %{y} laps"
                "<extra></extra>"),)

        st.plotly_chart(chart,
            use_container_width=True,
            config={"displayModeBar": False,})

    st.dataframe(stint_df,
        use_container_width=True,
        hide_index=True,)

    st.html(f"""
    <div class="section">

        <div class="section-kicker">
            CALIBRATION READOUT
        </div>

        <div class="section-title">
            What enters the simulator
        </div>

        <div class="interpretation">

            <div class="readout-row">

                <div class="readout-index">
                    01
                </div>

                <div>
                    <div class="readout-heading">
                        Historical foundation
                    </div>

                    <div class="readout-text">
                        The current calibration uses
                        <strong>{len(laps):,} historical lap records</strong>
                        across the selected seasons
                        <strong>{season_text}</strong>.
                    </div>
                </div>

            </div>

            <div class="readout-row">

                <div class="readout-index">
                    02
                </div>

                <div>
                    <div class="readout-heading">
                        Track-specific behaviour
                    </div>

                    <div class="readout-text">
                        Observed pace and stint information are used
                        alongside the calibrated track object to represent
                        the circuit inside the simulation environment.
                    </div>
                </div>

            </div>

            <div class="readout-row">

                <div class="readout-index">
                    03
                </div>

                <div>
                    <div class="readout-heading">
                        Simulation dependency
                    </div>

                    <div class="readout-text">
                        These calibrated parameters are subsequently passed
                        into the Monte Carlo simulation and strategy
                        optimisation pipeline.
                    </div>
                </div>

            </div>

        </div>

    </div>
    """)