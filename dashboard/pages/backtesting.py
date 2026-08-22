import streamlit as st
import pandas as pd

from dashboard.utils.backtest_runner import Backtesting


def show():

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    with open("dashboard/styles/backtesting.css", "r", encoding="utf-8") as f:
        st.html(f"<style>{f.read()}</style>")

    with st.spinner("Running historical backtest..."):
        results = Backtesting()

    df = pd.DataFrame(results)

    if df.empty:
        st.error("No backtesting results are available.")
        return

    race_name = st.session_state["race_name"]
    driver_code = st.session_state.get("driver_code", "N/A")

    st.html(f"""
    <div class="backtest-header">

        <div class="backtest-kicker">
            <span>●</span>
            HISTORICAL VALIDATION / BACKTESTING
        </div>

        <div class="backtest-title">
            Test the<br>
            <span>strategy.</span>
        </div>

        <div class="backtest-description">
            The predicted strategy is replayed against historical race
            conditions to measure how closely the model's decisions
            align with what actually happened on track.
        </div>

        <div class="race-context">
            RACE&nbsp;&nbsp;
            <strong>{race_name}</strong>
            &nbsp;&nbsp;/&nbsp;&nbsp;
            DRIVER&nbsp;&nbsp;
            <strong>{driver_code}</strong>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            VALIDATION OVERVIEW
        </div>

        <div class="section-title">
            How did the model perform?
        </div>

    </div>
    """)

    average_pit_error = df["Pit Window Error"].mean()

    if "Compound Match" in df.columns:
        compound_matches = df["Compound Match"].astype(str)
        compound_match_rate = (compound_matches
            .str.extract(r"(\d+)\s*/\s*(\d+)")[0]
            .astype(float)
            .div(compound_matches
                .str.extract(r"(\d+)\s*/\s*(\d+)")[1]
                .astype(float))
            .mean()
            * 100)
    else:
        compound_match_rate = None

    st.html(f"""
    <div class="metric-grid">

        <div class="metric-card">
            <div class="metric-label">
                AVERAGE PIT WINDOW ERROR
            </div>

            <div class="metric-value">
                {average_pit_error:.2f}
            </div>

            <div class="metric-unit">
                LAPS
            </div>
        </div>

        <div class="metric-card">
            <div class="metric-label">
                HISTORICAL RACES
            </div>

            <div class="metric-value">
                {len(df)}
            </div>

            <div class="metric-unit">
                SEASONS TESTED
            </div>
        </div>

        <div class="metric-card">
            <div class="metric-label">
                COMPOUND MATCH
            </div>

            <div class="metric-value">
                {f"{compound_match_rate:.1f}%" if compound_match_rate is not None else "N/A"}
            </div>

            <div class="metric-unit">
                STRATEGY ALIGNMENT
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            HISTORICAL RESULTS
        </div>

        <div class="section-title">
            Prediction vs reality
        </div>

        <div class="section-note">
            EACH ROW REPRESENTS ONE HISTORICAL SEASON USED TO TEST THE MODEL.
        </div>

    </div>
    """)

    st.dataframe(df, use_container_width=True, hide_index=True,)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            MODEL READOUT
        </div>

        <div class="section-title">
            What the backtest tells us
        </div>

        <div class="interpretation">
            Backtesting provides a historical reality check for the
            probabilistic strategy engine.

            <br><br>

            A smaller pit-window error indicates that the optimiser is
            identifying pit-stop timing closer to the strategy observed
            in historical race conditions.

            <br><br>

            <strong>
                The objective is not to reproduce history perfectly,
                but to determine whether the model produces decisions
                that remain credible outside the original simulation.
            </strong>
        </div>

    </div>
    """)