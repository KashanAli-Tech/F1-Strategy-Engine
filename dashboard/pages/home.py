import streamlit as st


def show():

    st.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

        :root {
            --bg: #0d0e12;
            --panel: #15171c;
            --text: #f2f3f5;
            --muted: #8d929b;
            --line: rgba(255,255,255,0.10);
            --red: #e10600;
        }

        .stApp {
            background:
                linear-gradient(rgba(13,14,18,0.96), rgba(13,14,18,0.96)),
                repeating-linear-gradient(
                    135deg,
                    rgba(255,255,255,0.025) 0px,
                    rgba(255,255,255,0.025) 1px,
                    transparent 1px,
                    transparent 6px
                );
        }

        .hero {
            position: relative;
            padding: 65px 0 55px;
            border-bottom: 1px solid var(--line);
            overflow: hidden;
        }

        .hero-grid {
            position: absolute;
            inset: 0;
            opacity: 0.11;
            background-image:
                linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px);
            background-size: 60px 60px;
            mask-image: linear-gradient(to right, black, transparent 82%);
        }

        .hero-kicker,
        .mono {
            font-family: 'JetBrains Mono', monospace;
        }

        .hero-kicker {
            position: relative;
            color: var(--muted);
            font-size: 0.72rem;
            letter-spacing: 0.16em;
            margin-bottom: 18px;
        }

        .hero-kicker span {
            color: var(--red);
        }

        .hero-title {
            position: relative;
            max-width: 950px;
            font-family: 'Chakra Petch', sans-serif;
            font-size: clamp(3.5rem, 7vw, 7.5rem);
            font-weight: 700;
            line-height: 0.88;
            letter-spacing: -0.055em;
            text-transform: uppercase;
        }

        .hero-title .red {
            color: var(--red);
        }

        .hero-text {
            position: relative;
            max-width: 650px;
            margin-top: 30px;
            color: var(--muted);
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.05rem;
            line-height: 1.65;
        }

        .telemetry {
            display: grid;
            grid-template-columns: 1.2fr 1fr 1fr 1fr;
            border-bottom: 1px solid var(--line);
            font-family: 'JetBrains Mono', monospace;
        }

        .telemetry-item {
            position: relative;
            min-height: 105px;
            padding: 22px 25px;
            border-right: 1px solid var(--line);
        }

        .telemetry-item:last-child {
            border-right: none;
        }

        .telemetry-label {
            margin-bottom: 10px;
            color: #666b74;
            font-size: 0.64rem;
            letter-spacing: 0.1em;
        }

        .telemetry-value {
            margin-bottom: 8px;
            color: var(--text);
            font-size: 1.25rem;
            font-weight: 600;
        }

        .telemetry-value.red {
            color: var(--red);
        }

        .status-dot {
            position: absolute;
            top: 20px;
            right: 18px;
            width: 7px;
            height: 7px;
            background: var(--red);
            box-shadow: 0 0 10px rgba(225,6,0,0.7);
        }

        .section {
            padding: 60px 0;
            border-bottom: 1px solid var(--line);
        }

        .section-title {
            margin-bottom: 8px;
            color: var(--text);
            font-family: 'Chakra Petch', sans-serif;
            font-size: 2.2rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            text-transform: uppercase;
        }

        .section-label {
            margin-bottom: 32px;
            color: #666b74;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.08em;
        }

        .copy p {
            color: #a7abb2;
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.05rem;
            line-height: 1.7;
        }

        .copy strong {
            color: var(--text);
        }

        .model-panel {
            position: relative;
            min-height: 300px;
            overflow: hidden;
            border: 1px solid var(--line);
            background:
                linear-gradient(
                    90deg,
                    transparent 49.5%,
                    rgba(255,255,255,0.06) 50%,
                    transparent 50.5%
                ),
                linear-gradient(
                    transparent 49.5%,
                    rgba(255,255,255,0.06) 50%,
                    transparent 50.5%
                );
            background-size: 80px 80px;
        }

        .model-panel::before {
            content: "";
            position: absolute;
            top: 52%;
            left: -20%;
            width: 140%;
            height: 2px;
            background: var(--red);
            transform: rotate(-8deg);
            opacity: 0.8;
        }

        .model-panel::after {
            content: "";
            position: absolute;
            top: -15%;
            left: 62%;
            width: 2px;
            height: 130%;
            background: rgba(255,255,255,0.15);
            transform: rotate(8deg);
        }

        .panel-label {
            position: absolute;
            top: 18px;
            left: 20px;
            color: #666b74;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.64rem;
            letter-spacing: 0.1em;
        }

        .panel-readout {
            position: absolute;
            right: 22px;
            bottom: 20px;
            color: var(--text);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            text-align: right;
        }

        .panel-readout strong {
            color: var(--red);
            font-size: 1.45rem;
        }

        .process-row {
            display: grid;
            grid-template-columns: 80px 1fr 1fr;
            align-items: center;
            padding: 25px 0;
            border-top: 1px solid var(--line);
        }

        .process-number {
            color: var(--red);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
        }

        .process-name {
            color: var(--text);
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
        }

        .process-text {
            color: var(--muted);
            font-family: 'Chakra Petch', sans-serif;
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .cta {
            padding: 65px 0 30px;
        }

        .cta-title {
            color: var(--text);
            font-family: 'Chakra Petch', sans-serif;
            font-size: clamp(2.5rem, 5vw, 5rem);
            font-weight: 700;
            line-height: 0.95;
            text-transform: uppercase;
        }

        .cta-title span {
            color: var(--red);
        }

        .cta-text {
            margin-top: 18px;
            color: var(--muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.05em;
        }

        div.stButton > button {
            margin-top: 25px;
            border: none;
            border-radius: 0;
            background: var(--red);
            color: white;
            font-family: 'Chakra Petch', sans-serif;
            font-weight: 700;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            transform: skewX(-10deg);
            transition: 0.2s ease;
        }

        div.stButton > button:hover {
            background: #ff180f;
            transform: skewX(-10deg) translateY(-2px);
        }

        .footer {
            padding-top: 30px;
            color: #555a63;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.08em;
        }
    </style>
    """)

    # Hero

    st.html("""
    <div class="hero">
        <div class="hero-grid"></div>

        <div class="hero-kicker">
            <span>●</span>
            F1 PROBABILISTIC STRATEGY ENGINE
            &nbsp;/&nbsp;
            RACE INTELLIGENCE
        </div>

        <div class="hero-title">
            Think ahead.<br>
            <span class="red">Race smarter.</span>
        </div>

        <div class="hero-text">
            A race strategy engine built around historical data,
            tyre degradation and probabilistic simulation.
            Instead of asking what happened, it asks what could
            happen next.
        </div>
    </div>
    """)

    # Current engine status

    st.html("""
    <div class="telemetry">

        <div class="telemetry-item">
            <div class="telemetry-label">[ SIMULATION LOAD ]</div>
            <div class="telemetry-value">1,000+</div>
            <div class="telemetry-label">MONTE CARLO RUNS</div>
        </div>

        <div class="telemetry-item">
            <div class="telemetry-label">[ TYRE MODEL ]</div>
            <div class="telemetry-value">SOFT / MED / HARD</div>
            <div class="telemetry-label">COMPOUNDS</div>
        </div>

        <div class="telemetry-item">
            <div class="telemetry-label">[ CALIBRATION ]</div>
            <div class="telemetry-value">2022 → 2025</div>
            <div class="telemetry-label">HISTORICAL DATA</div>
        </div>

        <div class="telemetry-item">
            <div class="telemetry-label">[ ENGINE STATUS ]</div>
            <div class="telemetry-value red">READY</div>
            <div class="status-dot"></div>
            <div class="telemetry-label">SYSTEM ONLINE</div>
        </div>

    </div>
    """)

    # Model overview

    st.html("""
    <div class="section">
        <div class="section-title">Behind the pit wall</div>
        <div class="section-label">HOW THE MODEL THINKS</div>
    </div>
    """)

    left, right = st.columns([1.05, 0.95], gap="large")

    with left:
        st.html("""
        <div class="copy">

            <p>
                Every strategy starts with
                <strong>real race data</strong>.
                Historical laps are used to estimate tyre behaviour,
                pace and circuit characteristics.
            </p>

            <p>
                Those parameters feed into a
                <strong>probabilistic race model</strong>
                where traffic, weather, tyre performance and
                lap-to-lap variation can change the outcome.
            </p>

            <p>
                Thousands of races are simulated.
                The aim isn't simply to find the strategy that
                looks fastest on paper, but the one that remains
                competitive when the race doesn't go perfectly.
            </p>

        </div>
        """)

    with right:
        st.html("""
        <div class="model-panel">
            <div class="panel-label">
                MODEL VIEW / STRATEGY SPACE
            </div>

            <div class="panel-readout">
                SIMULATION<br>
                <strong>READY</strong><br>
                UNCERTAINTY → ACTIVE
            </div>
        </div>
        """)

    # Strategy pipeline

    st.html("""
    <div class="section">

        <div class="section-title">From data to the call</div>
        <div class="section-label">RACE STRATEGY PIPELINE</div>

        <div class="process-row">
            <div class="process-number">01</div>
            <div class="process-name">Historical data</div>
            <div class="process-text">
                Lap times, tyre usage, pit stops and circuit
                behaviour establish the baseline.
            </div>
        </div>

        <div class="process-row">
            <div class="process-number">02</div>
            <div class="process-name">Parameter estimation</div>
            <div class="process-text">
                Tyre degradation, pace and track characteristics
                are estimated from the historical data.
            </div>
        </div>

        <div class="process-row">
            <div class="process-number">03</div>
            <div class="process-name">Monte Carlo simulation</div>
            <div class="process-text">
                Candidate strategies are tested across
                thousands of possible race outcomes.
            </div>
        </div>

        <div class="process-row">
            <div class="process-number">04</div>
            <div class="process-name">Strategy selection</div>
            <div class="process-text">
                Expected pace, risk and consistency are combined
                to identify the strongest strategy.
            </div>
        </div>

    </div>
    """)

    # CTA

    st.html("""
    <div class="cta">

        <div class="cta-title">
            Ready for<br>
            <span>lights out?</span>
        </div>

        <div class="cta-text">
            BUILD A RACE SCENARIO / TEST THE STRATEGY / MAKE THE CALL
        </div>

    </div>
    """)

    if st.button(
        "Open Strategy Control Centre",
        type="primary",
        use_container_width=True
    ):
        st.session_state["current_page"] = "Strategy Input"
        st.rerun()

    st.html("""
    <div class="footer">
        F1 PROBABILISTIC STRATEGY OPTIMISER
        &nbsp;·&nbsp;
        HISTORICAL CALIBRATION
        &nbsp;·&nbsp;
        MONTE CARLO
        &nbsp;·&nbsp;
        STRATEGY ANALYSIS
    </div>
    """)
