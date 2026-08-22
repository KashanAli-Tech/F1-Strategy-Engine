import streamlit as st

from utils.engine_runner import run_strategy_engine


def load_styles():
    with open("dashboard/styles/strategy_optimiser.css", "r", encoding="utf-8") as file:
        st.html(f"<style>{file.read()}</style>")


def show():

    load_styles()

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    with st.spinner("Running strategy optimisation..."):
        engine = run_strategy_engine(
            st.session_state["race_name"],
            st.session_state["years"],
            st.session_state["driver_code"],
        )

    best_strategy = engine["best_strategy"]
    results = engine["results"]

    best_result = None
    for strategy, result in results:
        if strategy == best_strategy:
            best_result = result
            break

    if best_result is None:
        st.error("Unable to find evaluation results for the best strategy.")
        return

    pit_stops = best_strategy.pit_stops

    total_laps = 50

    st.html(f"""
    <div class="optimiser-header">

        <div class="optimiser-kicker">
            <span>●</span>
            STRATEGY OPTIMISATION / MONTE CARLO
        </div>

        <div class="optimiser-title">
            Find the<br>
            <span>strongest call.</span>
        </div>

        <div class="optimiser-description">
            The optimiser evaluates candidate race strategies across
            thousands of simulated outcomes, balancing expected race
            time against variation and consistency.
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
            RECOMMENDED STRATEGY
        </div>

        <div class="section-title">
            The call
        </div>

    </div>
    """)

    stints = []

    current_compound = best_strategy.starting_compound
    current_lap = 1

    for pit in pit_stops:

        stints.append({"compound": current_compound,
            "start": current_lap,
            "end": pit.lap,})

        current_compound = pit.new_compound
        current_lap = pit.lap

    stints.append({"compound": current_compound,
        "start": current_lap,
        "end": total_laps,})

    stint_html = ""
    marker_html = ""

    for stint in stints:

        start_position = ((stint["start"] - 1) /
            (total_laps - 1)
        ) * 100

        end_position = ((stint["end"] - 1) /
            (total_laps - 1)
        ) * 100

        width = end_position - start_position

        if stint["end"] == total_laps:
            width = 100 - start_position

        compound_class = stint["compound"].lower()

        centre_position = start_position + (width / 2)

        stint_html += f"""
        <div
            class="track-stint {compound_class}"
            style="
                left: {start_position}%;
                width: {width}%;
            "
        ></div>

        <div
            class="track-stint-label"
            style="left: {centre_position}%"
        >
            {stint["compound"]}
        </div>
        """

    for pit in pit_stops:

        pit_position = ((pit.lap - 1) /
            (total_laps - 1)
        ) * 100

        marker_html += f"""
        <div
            class="track-marker pit"
            style="left: {pit_position}%"
        ></div>

        <div
            class="track-marker-label pit-label"
            style="left: {pit_position}%"
        >
            PIT LAP {pit.lap}
        </div>
        """

    pit_laps = ", ".join(str(pit.lap) for pit in pit_stops)

    st.html(f"""
    <div class="strategy-panel">

        <div class="strategy-label">
            OPTIMISED RACE PLAN
        </div>

        <div class="strategy-status">
            ● SELECTED BY MONTE CARLO OPTIMISER
        </div>

        <div class="strategy-track">

            <div class="track-line"></div>

            {stint_html}

            {marker_html}

            <div class="track-endpoints">
                <span>START / LAP 1</span>
                <span>FINISH / LAP {total_laps}</span>
            </div>

        </div>

        <div class="strategy-summary">

            <div class="strategy-summary-item">
                <div class="strategy-summary-label">
                    STINTS
                </div>

                <div class="strategy-summary-value">
                    {len(stints)}
                </div>
            </div>

            <div class="strategy-summary-item">
                <div class="strategy-summary-label">
                    PIT STOPS
                </div>

                <div class="strategy-summary-value">
                    {len(pit_stops)}
                </div>
            </div>

            <div class="strategy-summary-item">
                <div class="strategy-summary-label">
                    PIT LAPS
                </div>

                <div class="strategy-summary-value">
                    {pit_laps if pit_laps else "NONE"}
                </div>
            </div>

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

    </div>
    """)

    st.html(f"""
    <div class="performance-grid">

        <div class="performance-item">
            <div class="performance-label">
                Average Race Time
            </div>

            <div class="performance-value">
                {best_result["average_time"]:.2f}s
            </div>
        </div>

        <div class="performance-item">
            <div class="performance-label">
                Best Case
            </div>

            <div class="performance-value">
                {best_result["best_time"]:.2f}s
            </div>
        </div>

        <div class="performance-item">
            <div class="performance-label">
                Variation
            </div>

            <div class="performance-value">
                {best_result["variation"]:.4f}
            </div>
        </div>

        <div class="performance-item">
            <div class="performance-label">
                Consistency Score
            </div>

            <div class="performance-value">
                {best_result["consistency_score"]:.4f}
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            CANDIDATE STRATEGIES
        </div>

        <div class="section-title">
            Strategy comparison
        </div>

        <div class="comparison-note">
            EACH STRATEGY REPRESENTS A DIFFERENT RACE PLAN EVALUATED BY THE ENGINE.
        </div>

    </div>
    """)

    comparison_data = []

    for strategy, result in results:
        compounds = strategy.starting_compound

        for pit in strategy.pit_stops:
            compounds += f" → {pit.new_compound}"

        strategy_pit_laps = ", ".join(str(pit.lap) for pit in strategy.pit_stops)

        comparison_data.append({"Strategy": compounds,
            "Pit Laps": strategy_pit_laps,
            "Average Time": round(
                result["average_time"],
                2,
            ),
            "Risk": round(
                result["variation"],
                4,
            ),
            "Consistency": round(
                result["consistency_score"],
                4,),})

    st.dataframe(comparison_data, use_container_width=True, hide_index=True,)

    st.html("""
    <div class="section">

        <div class="section-kicker">
            MODEL INTERPRETATION
        </div>

        <div class="section-title">
            Why this strategy?
        </div>

        <div class="interpretation">

            The selected strategy represents the strongest balance between
            expected race performance and consistency across the simulated
            outcomes.

            <br><br>

            Unlike a deterministic calculation, the optimiser allows
            uncertainty in tyre performance, race conditions and
            lap-to-lap variation to influence the result.

            <br><br>

            <strong>
                The fastest theoretical strategy is not necessarily the
                strongest strategy when the race becomes unpredictable.
            </strong>

        </div>

    </div>
    """)