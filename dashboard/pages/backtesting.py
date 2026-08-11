import streamlit as st
import pandas as pd

from dashboard.utils.backtest_runner import Backtesting


def show():

    if not st.session_state["race_name"]:
        st.warning("Configure a race in Strategy Input before opening this page.")
        st.stop()

    st.title("Backtesting")
    st.write("""This backtests the predicted strategy from the optimisation engine against historical race strategies.""")

    with st.spinner("Running Backtester..."):
        results = Backtesting()

    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)
    st.divider()


    st.metric("Average Pit Window Error", f"{df['Pit Window Error'].mean():.2f} laps")