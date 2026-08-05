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
from configs.simulation_config import YEARS

@st.cache_data(show_spinner=False)
def run_strategy_engine():

    driver = Driver(name="Max Verstappen",
        pace=0.98,
        consistency=0.97,
        tyre_management=0.95,)


    track = Track(name="Silverstone",
        number_of_laps=50,
        base_lap_time=90,
        fuel_effect_per_lap=0.035,
        tyre_wear_multiplier=1.15,
        track_evolution_rate=0.01,)


    loader = HistoricalLoader()
    laps = loader.load(years=YEARS,
        race_name="British Grand Prix",
        driver="VER")

    tyre_estimator = TyreEstimator()
    degradation = tyre_estimator.estimate_degradation(laps)
    estimator = ParameterEstimator()
    calibrator = ParameterCalibrator()
    track = calibrator.calibrate_track(track,estimator, laps)

    optimiser = StrategyOptimiser(degradation)
    best_strategy, results = optimiser.optimise(driver, track)
    return {"driver": driver,
    "track": track,
    "laps": laps,
    "degradation": degradation,
    "best_strategy": best_strategy,
    "results": results}