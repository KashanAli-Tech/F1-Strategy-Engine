import streamlit as st

from pages import (
    home,
    strategy_input,
    strategy_optimiser,
    monte_carlo,
    backtesting,
    tyre_analysis,
    calibration,
)


st.set_page_config(
    page_title="F1 Probabilistic Strategy Optimiser",
    page_icon="🏎️",
    layout="wide",
)


if "race_name" not in st.session_state:
    st.session_state["race_name"] = None

if "years" not in st.session_state:
    st.session_state["years"] = []

if "driver_code" not in st.session_state:
    st.session_state["driver_code"] = None


pages = [
    st.Page(
        home.show,
        title="Home",
        url_path="home",
    ),
    st.Page(
        strategy_input.show,
        title="Strategy Input",
        url_path="strategy_input",
    ),
    st.Page(
        strategy_optimiser.show,
        title="Strategy Optimiser",
        url_path="strategy_optimiser",
    ),
    st.Page(
        monte_carlo.show,
        title="Monte Carlo Results",
        url_path="monte_carlo",
    ),
    st.Page(
        backtesting.show,
        title="Backtester",
        url_path="backtesting",
    ),
    st.Page(
        tyre_analysis.show,
        title="Tyre Degradation",
        url_path="tyre_analysis",
    ),
    st.Page(
        calibration.show,
        title="Track Calibration",
        url_path="calibration",
    ),
]


page = st.navigation(
    pages,
    position="hidden",
)


st.html("""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap'
);

:root {
    --carbon: #0D0E12;
    --white: #F2F3F5;
    --muted: #8D929B;
    --line: rgba(255,255,255,0.08);
    --red: #E10600;
}

[data-testid="stSidebar"] {
    background: var(--carbon);
    border-right: 1px solid var(--line);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

.sidebar-brand {
    padding: 0 0 24px 0;
    margin-bottom: 24px;
    border-bottom: 1px solid var(--line);
}

.sidebar-kicker {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.62rem;
    letter-spacing: 0.16em;
    color: #686D76;
    margin-bottom: 9px;
}

.sidebar-title {
    font-family: "Chakra Petch", sans-serif;
    font-size: 1.65rem;
    font-weight: 700;
    line-height: 0.95;
    text-transform: uppercase;
    color: var(--white);
}

.sidebar-title span {
    color: var(--red);
}

.sidebar-section {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    color: #555A63;
    margin-bottom: 10px;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] {
    margin-bottom: 2px;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    position: relative;
    display: flex;
    align-items: center;
    padding: 9px 11px;
    border-radius: 0;
    color: #9A9FA8;
    font-family: "Chakra Petch", sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    text-decoration: none;
    transition:
        background 0.18s ease,
        color 0.18s ease,
        padding-left 0.18s ease;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: rgba(255,255,255,0.045);
    color: var(--white);
    padding-left: 15px;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a::before {
    content: "";
    width: 3px;
    height: 0;
    position: absolute;
    left: 0;
    background: var(--red);
    transition: height 0.18s ease;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover::before {
    height: 65%;
}

.sidebar-footer {
    margin-top: 30px;
    padding-top: 18px;
    border-top: 1px solid var(--line);
    font-family: "JetBrains Mono", monospace;
    font-size: 0.58rem;
    line-height: 1.9;
    letter-spacing: 0.05em;
    color: #555A63;
}

.sidebar-footer span {
    color: #777C85;
}

</style>
""")


with st.sidebar:

    st.html("""
    <div class="sidebar-brand">

        <div class="sidebar-kicker">
            RACE INTELLIGENCE / 01
        </div>

        <div class="sidebar-title">
            F1 <span>Strategy</span><br>
            Engine
        </div>
    </div>
    """)

    st.html("""
    <div class="sidebar-section">
        NAVIGATION
    </div>
    """)

    st.page_link(pages[0], label="Home")
    st.page_link(pages[1], label="Strategy Input")
    st.page_link(pages[2], label="Strategy Optimiser")
    st.page_link(pages[3], label="Monte Carlo Results")
    st.page_link(pages[4], label="Backtester")
    st.page_link(pages[5], label="Tyre Degradation")
    st.page_link(pages[6], label="Track Calibration")

    st.html("""
    <div class="sidebar-footer">
        MODEL&nbsp;&nbsp;&nbsp; <span>MONTE CARLO</span><br>
        DATA&nbsp;&nbsp;&nbsp;&nbsp; <span>HISTORICAL F1</span>
    </div>
    """)


page.run()