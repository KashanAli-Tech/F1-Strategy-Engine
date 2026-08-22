import streamlit as st
import pandas as pd
import plotly.express as px

from utils.engine_runner import run_strategy_engine


def show():

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    with open("dashboard/styles/tyre_analysis.css", "r", encoding="utf-8") as f:
        st.html(f"<style>{f.read()}</style>")

    with st.spinner("Analysing historical tyre performance..."):
        engine = run_strategy_engine(st.session_state["race_name"],st.session_state["years"],st.session_state["driver_code"],
)

    degradation = engine["degradation"]

    degradation_df = pd.DataFrame({"Compound": list(degradation.keys()),
        "Degradation (seconds/lap)": list(degradation.values()),})

    best = degradation_df.loc[degradation_df["Degradation (seconds/lap)"].idxmin()]
    worst = degradation_df.loc[degradation_df["Degradation (seconds/lap)"].idxmax()]
    average_degradation = degradation_df["Degradation (seconds/lap)"].mean()

    st.html(f"""
    <div class="tyre-header">

        <div class="tyre-kicker">
            <span>●</span>
            TYRE PERFORMANCE / HISTORICAL MODEL
        </div>

        <div class="tyre-title">
            Read the<br>
            <span>rubber.</span>
        </div>

        <div class="tyre-description">
            Historical lap data is used to estimate how quickly each
            compound loses performance as tyre age increases during a stint.
            These degradation rates feed directly into the strategy engine.
        </div>

        <div class="race-context">
            RACE&nbsp;&nbsp;
            <strong>{st.session_state["race_name"]}</strong>
            &nbsp;&nbsp;/&nbsp;&nbsp;
            DRIVER&nbsp;&nbsp;
            <strong>{st.session_state["driver_code"]}</strong>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            DEGRADATION PROFILE
        </div>

        <div class="section-title">
            How quickly does performance fall?
        </div>

    </div>
    """)

    st.html(f"""
    <div class="degradation-grid">

        <div class="degradation-card">

            <div class="card-label">
                LOWEST DEGRADATION
            </div>

            <div class="compound-name">
                {best["Compound"]}
            </div>

            <div class="compound-rate">
                {best["Degradation (seconds/lap)"]:.4f}
                <span>s / LAP</span>
            </div>

            <div class="card-status">
                ● STRONGEST LONG-STINT PROFILE
            </div>

        </div>

        <div class="degradation-card">

            <div class="card-label">
                HIGHEST DEGRADATION
            </div>

            <div class="compound-name">
                {worst["Compound"]}
            </div>

            <div class="compound-rate">
                {worst["Degradation (seconds/lap)"]:.4f}
                <span>s / LAP</span>
            </div>

            <div class="card-status warning">
                ● FASTEST PERFORMANCE LOSS
            </div>

        </div>

        <div class="degradation-card">

            <div class="card-label">
                MODEL AVERAGE
            </div>

            <div class="compound-name">
                {average_degradation:.4f}
            </div>

            <div class="compound-rate">
                s / LAP
            </div>

            <div class="card-status neutral">
                HISTORICAL ESTIMATE
            </div>

        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            COMPOUND ANALYSIS
        </div>

        <div class="section-title">
            Degradation by compound
        </div>

        <div class="section-note">
            LOWER VALUES INDICATE SLOWER LAP-TIME DEGRADATION AS TYRE AGE INCREASES.
        </div>

    </div>
    """)

    chart = px.bar(degradation_df, x="Compound", y="Degradation (seconds/lap)",)

    chart.update_layout(title="",
        template="plotly_dark",
        showlegend=False,
        paper_bgcolor="#13151A",
        plot_bgcolor="#13151A",
        font=dict(family="JetBrains Mono", color="#8D929B",),
        margin=dict(l=25,r=25,t=25,b=25,),
        xaxis=dict(title="", gridcolor="rgba(255,255,255,0.04)", zeroline=False,),
        yaxis=dict(title="Seconds lost per lap", gridcolor="rgba(255,255,255,0.06)", zeroline=False,),)

    chart.update_traces(marker_color="#E10600",
        marker_line_width=0,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Degradation: %{y:.4f}s/lap"
            "<extra></extra>"),)

    st.plotly_chart(chart,
        use_container_width=True,
        config={"displayModeBar": False,},)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            RAW MODEL OUTPUT
        </div>

        <div class="section-title">
            Estimated rates
        </div>

    </div>
    """)

    st.dataframe(degradation_df, use_container_width=True, hide_index=True,)

    st.html(f"""
    <div class="section">

        <div class="section-kicker">
            MODEL INTERPRETATION
        </div>

        <div class="section-title">
            What the data suggests
        </div>

        <div class="interpretation">

            <div class="interpretation-row">

                <div class="interpretation-index">
                    01
                </div>

                <div>
                    <div class="interpretation-heading">
                        {best["Compound"]} holds performance longest
                    </div>

                    <div class="interpretation-text">
                        The model estimates degradation of
                        <strong>{best["Degradation (seconds/lap)"]:.4f}s per lap</strong>,
                        giving it the lowest predicted performance loss
                        as the stint progresses.
                    </div>
                </div>

            </div>

            <div class="interpretation-row">

                <div class="interpretation-index">
                    02
                </div>

                <div>
                    <div class="interpretation-heading">
                        {worst["Compound"]} loses performance fastest
                    </div>

                    <div class="interpretation-text">
                        Its estimated degradation of
                        <strong>{worst["Degradation (seconds/lap)"]:.4f}s per lap</strong>
                        makes tyre age a more significant factor when
                        considering longer stints.
                    </div>
                </div>

            </div>

            <div class="interpretation-row">

                <div class="interpretation-index">
                    03
                </div>

                <div>
                    <div class="interpretation-heading">
                        Why this matters to the optimiser
                    </div>

                    <div class="interpretation-text">
                        These estimates become inputs to the probabilistic
                        strategy engine, allowing different pit windows and
                        compound sequences to be evaluated under simulated
                        race conditions.
                    </div>
                </div>

            </div>

        </div>

    </div>
    """)