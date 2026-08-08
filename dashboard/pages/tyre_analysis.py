import streamlit as st
import pandas as pd
import plotly.express as px

from utils.engine_runner import run_strategy_engine

def show():
    st.title("Tyre Degradation Analysis")
    st.write("""This page presents tyre degradation estimates calculated from historical Formula 1 lap data.
    Degradation represents the expected lap time loss as tyre age increases during a stint.""")
    st.divider()

    engine = run_strategy_engine(st.session_state["race_name"], st.session_state["years"], st.session_state["driver_code"])
    degradation = engine["degradation"]
    st.subheader("Estimated Degradation Rates")
    degradation_df = pd.DataFrame({"Compound": list(degradation.keys()), "Degradation (seconds/lap)": list(degradation.values())})
    st.dataframe(degradation_df, use_container_width=True)
    st.divider()

    st.subheader("Compound Comparison")
    chart = px.bar(degradation_df, x="Compound", y="Degradation (seconds/lap)", title="Estimated Tyre Degradation")
    st.plotly_chart(chart, use_container_width=True)
    st.divider()

    st.subheader("Model Interpretation")
    best = degradation_df.loc[degradation_df["Degradation (seconds/lap)"].idxmin()]
    worst = degradation_df.loc[degradation_df["Degradation (seconds/lap)"].idxmax()]
    st.write(f"""The compound with the lowest estimated degradation is:

        **{best['Compound']}**
        ({best['Degradation (seconds/lap)']:.4f}s/lap)


        The compound with the highest estimated degradation is:

        **{worst['Compound']}**
        ({worst['Degradation (seconds/lap)']:.4f}s/lap)


        These estimates are generated from historical race data and are used by the strategy optimisation engine.
        """
    )