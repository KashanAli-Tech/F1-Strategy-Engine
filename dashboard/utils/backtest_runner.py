import streamlit as st

from src.backtesting.backtester import Backtester
from utils.engine_runner import run_strategy_engine
from src.strategy.strategy_evaluator import StrategyEvaluator


def Backtesting():

    race_name = st.session_state["race_name"]
    years = st.session_state["years"]
    driver_code = st.session_state["driver_code"]

    engine = run_strategy_engine(race_name, years, driver_code)
    best_strategy = engine["best_strategy"]
    results = engine["results"]
    laps = engine["laps"]
    predicted_result = None

    for strategy, result in results:
        if strategy == best_strategy:
            predicted_result = result
            break

    if predicted_result is None:
        raise ValueError("Could not find the Monte Carlo result for the recommended strategy.")
    
    backtester = Backtester()
    evaluator = StrategyEvaluator()
    backtest_results = []
    historical_laps = {year: laps[laps["Year"] == year].copy() for year in years}

    for year, season_laps in historical_laps.items():

        if season_laps.empty:
            raise ValueError(f"No historical lap data found for "
                f"{race_name} in {year} for driver {driver_code}.")

        result = backtester.evaluate(strategy=best_strategy,
            historical_laps=season_laps,
            predicted_result=predicted_result)

        backtest_results.append({"Year": year,
            "Strategy": evaluator.format_strategy(result["strategy"]),
            "Predicted Pit Laps": result["predicted_pit_laps"],
            "Actual Pit Laps": result["actual_pit_laps"],
            "Pit Window Error": result["pit_window_error"],
            "Predicted Compounds": result["predicted_compounds"],
            "Historical Compounds": result["actual_compounds"],
            "Compound Match":
                f"{result['compound_match']['matches']} / "
                f"{result['compound_match']['total']}"})

    return backtest_results