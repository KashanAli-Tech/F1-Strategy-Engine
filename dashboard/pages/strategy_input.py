import streamlit as st

from utils.race_config import (
    get_races,
    get_available_years,
    get_drivers,
)


def show():

    st.html("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        --carbon: #0D0E12;
        --panel: #13161B;
        --panel-light: #181B21;
        --white: #F2F3F5;
        --muted: #8D929B;
        --dim: #5F646D;
        --line: rgba(255,255,255,0.09);
        --red: #E10600;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 85% 15%,
                rgba(225, 6, 0, 0.055),
                transparent 28%
            ),
            #0D0E12;
    }

    .input-header {
        padding: 38px 0 32px 0;
        border-bottom: 1px solid var(--line);
    }

    .input-kicker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.16em;
        color: var(--dim);
        margin-bottom: 12px;
    }

    .input-kicker span {
        color: var(--red);
    }

    .input-title {
        font-family: 'Chakra Petch', sans-serif;
        font-size: clamp(2.8rem, 5vw, 5rem);
        font-weight: 700;
        line-height: 0.95;
        letter-spacing: -0.045em;
        text-transform: uppercase;
        color: var(--white);
    }

    .input-title span {
        color: var(--red);
    }

    .input-intro {
        max-width: 720px;
        margin-top: 18px;
        font-family: 'Chakra Petch', sans-serif;
        font-size: 1rem;
        line-height: 1.6;
        color: var(--muted);
    }

    .section-kicker {
        margin-top: 34px;
        margin-bottom: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.14em;
        color: var(--red);
    }

    .section-title {
        font-family: 'Chakra Petch', sans-serif;
        font-size: 1.9rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: -0.025em;
        color: var(--white);
        margin-bottom: 6px;
    }

    .section-description {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        line-height: 1.6;
        color: var(--dim);
        margin-bottom: 20px;
    }

    .race-panel {
        display: grid;
        grid-template-columns: 1fr 1.05fr;
        min-height: 285px;
        background: #111419;
        border: 1px solid var(--line);
        overflow: hidden;
    }

    .race-details {
        padding: 30px;
        border-right: 1px solid var(--line);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .race-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.13em;
        color: var(--dim);
        margin-bottom: 8px;
    }

    .race-name {
        font-family: 'Chakra Petch', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        line-height: 1;
        color: var(--white);
        text-transform: uppercase;
    }

    .race-season {
        margin-top: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: var(--muted);
    }

    .race-meta {
        display: flex;
        gap: 28px;
        margin-top: 30px;
    }

    .race-meta-item {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        color: var(--dim);
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .race-meta-item strong {
        display: block;
        color: var(--white);
        font-size: 0.82rem;
        margin-top: 5px;
    }

    .track-space {
        position: relative;
        min-height: 285px;
        background:
            linear-gradient(
                rgba(255,255,255,0.035) 1px,
                transparent 1px
            ),
            linear-gradient(
                90deg,
                rgba(255,255,255,0.035) 1px,
                transparent 1px
            );
        background-size: 38px 38px;
        overflow: hidden;
    }

    .track-space::before {
        content: "";
        position: absolute;
        width: 70%;
        height: 140%;
        left: 12%;
        top: -20%;
        border: 2px solid rgba(225,6,0,0.45);
        border-radius: 48% 52% 42% 58%;
        transform: rotate(-16deg);
    }

    .track-space::after {
        content: "";
        position: absolute;
        width: 42%;
        height: 80%;
        left: 28%;
        top: 10%;
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 50%;
        transform: rotate(18deg);
    }

    .track-placeholder {
        position: absolute;
        right: 20px;
        bottom: 18px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58rem;
        letter-spacing: 0.1em;
        color: #555A63;
        z-index: 2;
    }

    .driver-panel {
        background: #111419;
        border: 1px solid var(--line);
        min-height: 210px;
        overflow: hidden;
        display: grid;
        grid-template-columns: 0.85fr 1.15fr;
    }

    .driver-image {
        position: relative;
        min-height: 210px;
        background:
            linear-gradient(
                135deg,
                rgba(225,6,0,0.12),
                transparent 55%
            ),
            #15181D;
        border-right: 1px solid var(--line);
    }

    .driver-image::before {
        content: "";
        position: absolute;
        width: 130px;
        height: 170px;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -45%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 50% 50% 12px 12px;
    }

    .driver-image-label {
        position: absolute;
        left: 18px;
        bottom: 16px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58rem;
        color: var(--dim);
        letter-spacing: 0.1em;
    }

    .driver-info {
        padding: 25px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .driver-code {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        color: var(--red);
        letter-spacing: 0.13em;
        margin-bottom: 8px;
    }

    .driver-name {
        font-family: 'Chakra Petch', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--white);
    }

    .driver-note {
        margin-top: 8px;
        font-family: 'Chakra Petch', sans-serif;
        font-size: 0.9rem;
        line-height: 1.5;
        color: var(--muted);
    }

    .control-panel {
        padding: 24px;
        background: #111419;
        border: 1px solid var(--line);
    }

    .control-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.11em;
        color: var(--dim);
        margin-bottom: 14px;
    }

    .config-strip {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        border: 1px solid var(--line);
        background: #111419;
    }

    .config-item {
        padding: 18px 20px;
        border-right: 1px solid var(--line);
    }

    .config-item:last-child {
        border-right: none;
    }

    .config-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58rem;
        color: var(--dim);
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .config-value {
        margin-top: 7px;
        font-family: 'Chakra Petch', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        color: var(--white);
    }

    .run-panel {
        margin-top: 35px;
        padding: 28px;
        background:
            linear-gradient(
                110deg,
                rgba(225,6,0,0.08),
                transparent 55%
            ),
            #111419;
        border: 1px solid var(--line);
    }

    .run-title {
        font-family: 'Chakra Petch', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--white);
    }

    .run-description {
        margin-top: 6px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        line-height: 1.6;
        color: var(--dim);
    }

    div.stButton > button {
        border-radius: 0;
        border: none;
        background: var(--red);
        color: white;
        font-family: 'Chakra Petch', sans-serif;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        transform: skewX(-8deg);
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        background: #ff180f;
        transform: skewX(-8deg) translateY(-2px);
    }

    [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"],
    [data-testid="stSlider"] {
        font-family: 'Chakra Petch', sans-serif;
    }

    </style>
    """)

    st.html("""
    <div class="input-header">

        <div class="input-kicker">
            <span>●</span>
            RACE CONFIGURATION / 02
        </div>

        <div class="input-title">
            Build the<br>
            <span>race scenario.</span>
        </div>

        <div class="input-intro">
            Set the conditions before the model gets involved.
            Choose the race, establish the historical baseline,
            then decide how you want the driver and strategy to behave.
        </div>

    </div>
    """)

    st.html("""
    <div class="section-kicker">01 / EVENT</div>

    <div class="section-title">
        Pick the race
    </div>

    <div class="section-description">
        THE CIRCUIT AND SEASON DEFINE THE BASELINE FOR THE SIMULATION
    </div>
    """)

    prediction_year = st.selectbox(
        "Prediction Season",
        [2022, 2023, 2024, 2025, 2026],
        index=4,
    )

    races = get_races(prediction_year)

    if not races:
        st.error("No races available for this season.")
        return

    selected_race = st.selectbox(
        "Grand Prix",
        races,
    )

    st.html(f"""
    <div class="race-panel">

        <div class="race-details">

            <div>
                <div class="race-label">
                    SELECTED EVENT
                </div>

                <div class="race-name">
                    {selected_race}
                </div>

                <div class="race-season">
                    {prediction_year} SEASON
                </div>
            </div>

            <div class="race-meta">

                <div class="race-meta-item">
                    MODE
                    <strong>PREDICTION</strong>
                </div>

                <div class="race-meta-item">
                    SOURCE
                    <strong>FASTF1</strong>
                </div>

                <div class="race-meta-item">
                    ENGINE
                    <strong>MONTE CARLO</strong>
                </div>

            </div>

        </div>

        <div class="track-space">
            <div class="track-placeholder">
                TRACK IMAGE / CIRCUIT MAP
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="section-kicker">02 / CALIBRATION</div>

    <div class="section-title">
        Give the model some history
    </div>

    <div class="section-description">
        PREVIOUS SEASONS ARE USED TO ESTIMATE PACE, TYRE BEHAVIOUR AND CIRCUIT CHARACTERISTICS
    </div>
    """)

    available_calibration_years = get_available_years(selected_race)

    calibration_years = [
        year
        for year in available_calibration_years
        if year < prediction_year
    ]

    if not calibration_years:
        st.error(
            f"No historical data is available for "
            f"{selected_race} before {prediction_year}."
        )
        return

    selected_years = st.multiselect(
        "Calibration Seasons",
        calibration_years,
        default=calibration_years,
        help=(
            "Historical seasons used to estimate tyre degradation, "
            "pace and track characteristics."
        ),
    )

    st.html("""
    <div class="section-kicker">03 / DRIVER</div>

    <div class="section-title">
        Who's behind the wheel?
    </div>

    <div class="section-description">
        DRIVER PARAMETERS CHANGE HOW THE SIMULATION TREATS PACE, CONSISTENCY AND TYRE USAGE
    </div>
    """)

    drivers = get_drivers(
        prediction_year,
        selected_race,
    )

    if not drivers:
        st.error("No drivers were found for this race.")
        return

    selected_driver_name = st.selectbox(
        "Driver",
        list(drivers.keys()),
    )

    selected_driver = drivers[selected_driver_name]

    st.html(f"""
    <div class="driver-panel">

        <div class="driver-image">
            <div class="driver-image-label">
                DRIVER IMAGE / 2026
            </div>
        </div>

        <div class="driver-info">

            <div class="driver-code">
                DRIVER PROFILE
            </div>

            <div class="driver-name">
                {selected_driver_name}
            </div>

            <div class="driver-note">
                The selected driver will be used as the
                pace and consistency baseline for the race model.
            </div>

        </div>

    </div>
    """)

    st.html("""
    <div class="control-panel">

        <div class="control-label">
            DRIVER CHARACTERISTICS
        </div>

    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:

        aggressiveness = st.slider(
            "Driving Aggressiveness",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help=(
                "Controls how aggressively the driver is assumed "
                "to approach tyre usage and race pace."
            ),
        )

    with col2:

        tyre_management = st.slider(
            "Tyre Management",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help=(
                "Controls the assumed ability to preserve tyre "
                "performance during a stint."
            ),
        )

    consistency = st.slider(
        "Driver Consistency",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
    )

    st.html("""
    <div class="section-kicker">04 / STRATEGY</div>

    <div class="section-title">
        Decide how aggressive the call should be
    </div>

    <div class="section-description">
        THESE SETTINGS CONTROL WHICH STRATEGIES THE OPTIMISER IS ALLOWED TO CONSIDER
    </div>
    """)

    preferred_compounds = st.multiselect(
        "Available Compounds",
        ["Soft", "Medium", "Hard"],
        default=["Soft", "Medium", "Hard"],
    )

    risk_tolerance = st.slider(
        "Strategy Risk Tolerance",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.1,
    )

    st.html("""
    <div class="section-kicker">05 / CONDITIONS</div>

    <div class="section-title">
        What does race day look like?
    </div>

    <div class="section-description">
        WEATHER CAN BE FIXED FOR A CONTROLLED TEST OR LEFT TO THE MODEL
    </div>
    """)

    weather_mode = st.selectbox(
        "Weather Scenario",
        [
            "Automatic",
            "Dry",
            "Light Rain",
            "Heavy Rain",
        ],
    )

    st.html("""
    <div class="section-kicker">06 / CURRENT CONFIGURATION</div>

    <div class="section-title">
        Race setup
    </div>
    """)

    st.html(f"""
    <div class="config-strip">

        <div class="config-item">
            <div class="config-label">
                GRAND PRIX
            </div>
            <div class="config-value">
                {selected_race}
            </div>
        </div>

        <div class="config-item">
            <div class="config-label">
                SEASON
            </div>
            <div class="config-value">
                {prediction_year}
            </div>
        </div>

        <div class="config-item">
            <div class="config-label">
                DRIVER
            </div>
            <div class="config-value">
                {selected_driver_name}
            </div>
        </div>

    </div>
    """)

    st.html("""
    <div class="run-panel">

        <div class="run-title">
            Ready to run the race?
        </div>

        <div class="run-description">
            CHECK THE SETTINGS ABOVE THEN SEND THE SCENARIO
            INTO THE STRATEGY ENGINE.
        </div>

    </div>
    """)

    if st.button(
        "🏁  Run Strategy Analysis",
        type="primary",
        use_container_width=True,
    ):

        if not selected_years:
            st.error("Select at least one calibration season.")
            return

        if not preferred_compounds:
            st.error("Select at least one tyre compound.")
            return

        st.session_state["prediction_year"] = prediction_year
        st.session_state["race_name"] = selected_race
        st.session_state["years"] = selected_years
        st.session_state["driver_code"] = selected_driver

        st.session_state["aggressiveness"] = aggressiveness
        st.session_state["consistency"] = consistency
        st.session_state["tyre_management"] = tyre_management

        st.session_state["preferred_compounds"] = preferred_compounds
        st.session_state["risk_tolerance"] = risk_tolerance
        st.session_state["weather_mode"] = weather_mode

        st.session_state["run_analysis"] = True

        st.success(
            f"Configuration ready: "
            f"{selected_driver_name} — "
            f"{selected_race} {prediction_year}"
        )

        st.info(
            f"Using {', '.join(map(str, selected_years))} "
            f"for historical calibration."
        )