import streamlit as st
import pandas as pd
import plotly.express as px

from utils.engine_runner import run_strategy_engine

def load_css():
    with open("dashboard/styles/monte_carlo.css", "r", encoding="utf-8") as file:
        st.html(f"<style>{file.read()}</style>")


def show():
    load_css()

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    with st.spinner("Running Monte Carlo simulation..."):
        engine = run_strategy_engine(st.session_state["race_name"], st.session_state["years"], st.session_state["driver_code"], )

    best_strategy = engine["best_strategy"]
    results = engine["results"]

    best_result = None

    for strategy, result in results:
        if strategy == best_strategy:
            best_result = result
            break

    if best_result is None:
        st.error("Simulation results could not be loaded.")
        return

    race_times = best_result["race_times"]

    st.html(f"""
    <div class="mc-header">

        <div class="mc-kicker">
            <span>●</span>
            MONTE CARLO / SIMULATION ANALYSIS
        </div>

        <div class="mc-title">
            Measure the<br>
            <span>uncertainty.</span>
        </div>

        <div class="mc-description">
            Thousands of simulated race outcomes are used to examine
            the distribution, variation and consistency of the selected
            strategy. The result is a probabilistic view of race
            performance rather than a single deterministic prediction.
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
            SIMULATION OUTPUT
        </div>

        <div class="section-title">
            Race performance
        </div>

        <div class="section-description">
            Summary statistics from the Monte Carlo runs for the
            strategy selected by the optimisation engine.
        </div>

    </div>
    """)

    st.html(f"""
    <div class="metric-grid">

        <div class="metric-item">
            <div class="metric-label">Average</div>
            <div class="metric-value">
                {best_result["average_time"]:.2f}s
            </div>
        </div>

        <div class="metric-item">
            <div class="metric-label">Best Case</div>
            <div class="metric-value">
                {best_result["best_time"]:.2f}s
            </div>
        </div>

        <div class="metric-item">
            <div class="metric-label">Worst Case</div>
            <div class="metric-value">
                {best_result["worst_time"]:.2f}s
            </div>
        </div>

        <div class="metric-item">
            <div class="metric-label">Variation</div>
            <div class="metric-value">
                {best_result["variation"]:.3f}
            </div>
        </div>

        <div class="metric-item">
            <div class="metric-label">Consistency</div>
            <div class="metric-value">
                {best_result["consistency_score"]:.4f}
            </div>
        </div>

    </div>
    """)

    df = pd.DataFrame({
        "Race Time (s)": race_times
    })

    st.html("""
    <div class="section">

        <div class="section-kicker">
            OUTCOME DISTRIBUTION
        </div>

        <div class="section-title">
            Where does the race land?
        </div>

        <div class="section-description">
            The distribution shows how frequently the simulation
            produces different race times. A tighter distribution
            indicates more predictable performance.
        </div>

    </div>
    """)

    histogram = px.histogram(df, x="Race Time (s)", nbins=30,)

    histogram.update_layout(template="plotly_dark",
        title="",
        xaxis_title="Race Time (seconds)",
        yaxis_title="Simulation Frequency",
        showlegend=False,
        font=dict(
            family="JetBrains Mono",
            color="#8D929B",
        ),
        paper_bgcolor="#13151A",
        plot_bgcolor="#13151A",
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.06)",
            zeroline=False,
        ),
        yaxis=dict(
        title="Simulation Frequency",
        gridcolor="rgba(255,255,255,0.06)",
        zeroline=False,
        tickformat="d",
        rangemode="tozero",),)

    histogram.update_traces(marker_line_width=0,
        marker_color="#E10600",
        opacity=0.82,
        showlegend=False,
        hovertemplate="Race Time: %{x:.2f}s<br>Frequency: %{y}<extra></extra>",)

    st.html("""
    <div class="chart-panel">

        <div class="chart-label">
            MONTE CARLO OUTPUT
        </div>

        <div class="chart-title">
            Simulated race-time distribution
        </div>

    </div>
    """)

    st.plotly_chart(histogram,
        use_container_width=True,
        config={"displayModeBar": False},)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            PERFORMANCE SPREAD
        </div>

        <div class="section-title">
            How much can the result move?
        </div>

        <div class="section-description">
            The spread of simulated race times highlights the range
            of outcomes produced by the same strategy under changing
            race conditions and performance variation.
        </div>

    </div>
    """)

    box = px.box(df, y="Race Time (s)",)

    box.update_layout(template="plotly_dark",
        title=None,
        yaxis_title="Race Time (seconds)",
        font=dict(
            family="JetBrains Mono",
            color="#8D929B",
        ),
        paper_bgcolor="#13151A",
        plot_bgcolor="#13151A",
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.06)",
            zeroline=False,),
        xaxis=dict(
            showticklabels=False,
            gridcolor="rgba(255,255,255,0.06)",),)

    box.update_traces(marker_color="#E10600", line_color="#E10600",)

    st.html("""
    <div class="chart-panel">

        <div class="chart-label">
            RISK PROFILE
        </div>

        <div class="chart-title">
            Race-time spread
        </div>

    </div>
    """)

    st.plotly_chart(box, use_container_width=True, config={"displayModeBar": False},)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            SIMULATION RECORD
        </div>

        <div class="section-title">
            Statistical summary
        </div>

        <div class="section-description">
            Descriptive statistics for the simulated race-time
            distribution.
        </div>

    </div>
    """)

    summary = df.describe().round(3)

    st.html('<div class="summary-panel">')

    st.dataframe(summary, use_container_width=True, hide_index=False,)

    st.html("""
    </div>

    <div class="interpretation">

        The Monte Carlo simulation evaluates a large number of
        possible race outcomes rather than relying on one fixed
        prediction.

        <br><br>

        <strong>
            The distribution therefore gives a clearer picture of
            both expected performance and the uncertainty surrounding
            the strategy.
        </strong>

    </div>
    """)