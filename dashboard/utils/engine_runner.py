import sys
from pathlib import Path
import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))


from src.models.driver import Driver
from src.models.track import Track
from src.data.historical_loader import HistoricalLoader
from src.data.tyre_estimator import TyreEstimator
from src.data.parameter_estimator import ParameterEstimator
from src.data.calibrator import ParameterCalibrator
from src.strategy.strategy_optimiser import StrategyOptimiser


@st.cache_data(show_spinner=False)
def run_strategy_engine(race_name, years, driver_code):

    loader = HistoricalLoader()
    laps = loader.load(years=years, race_name=race_name, driver=driver_code)

    tyre_estimator = TyreEstimator()
    degradation = tyre_estimator.estimate_degradation(laps)

    track = Track(name=race_name,
        number_of_laps=50,
        base_lap_time=90,
        fuel_effect_per_lap=0.035,
        tyre_wear_multiplier=1.15,
        track_evolution_rate=0.01,)


    estimator = ParameterEstimator()

    calibrator = ParameterCalibrator()

    track = calibrator.calibrate_track(track, estimator, laps)

    driver = Driver(name=driver_code,
        pace=0.98,
        consistency=0.97,
        tyre_management=0.95,)

    optimiser = StrategyOptimiser(degradation)
    best_strategy, results = optimiser.optimise(driver, track)


    return {"driver": driver,
        "track": track,
        "laps": laps,
        "degradation": degradation,
        "best_strategy": best_strategy,
        "results": results}