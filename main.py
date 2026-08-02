from src.models.driver import Driver
from src.models.track import Track
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.strategy.strategy_optimiser import StrategyOptimiser
from src.simulation.monte_carlo import MonteCarloSimulator
from src.data.parameter_estimator import ParameterEstimator
from src.data.calibrator import ParameterCalibrator
from src.data.tyre_estimator import TyreEstimator
from src.data.historical_loader import HistoricalLoader
from src.evaluation.backtester import Backtester

if __name__ == "__main__":

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


    historical_loader = HistoricalLoader()

    laps = historical_loader.load(years=[2022, 2023, 2024],
        race_name="British Grand Prix",
        driver="VER")
    tyre_estimator = TyreEstimator()
    degradation = tyre_estimator.estimate_degradation(laps)

    print("\nTyre Degradation:")

    for compound, rate in degradation.items():
        print(f"{compound}: {rate:.4f}s/lap")

    estimator = ParameterEstimator()
    calibrator = ParameterCalibrator()
    track = calibrator.calibrate_track(track, estimator, laps)

    print("\nCalibrated Track: ")
    print(f"Base Lap Time: {track.base_lap_time:.3f}s")

    # strategy optimisation stuff
    optimiser = StrategyOptimiser(degradation)
    best_strategy, results = optimiser.optimise(driver, track)
    print("\nBest Pit Window For Each Strategy:\n")
    best_by_strategy = {}

    for strategy, analysis in results:

        base_strategy = optimiser.evaluator.format_strategy(strategy).split(" (Pit Lap")[0]

        if (base_strategy not in best_by_strategy or analysis["average_time"] < best_by_strategy[base_strategy]["average_time"]):
            best_by_strategy[base_strategy] = {"strategy": optimiser.evaluator.format_strategy(strategy),
                "average_time": analysis["average_time"],
                "variation": analysis["variation"]}

    for name, result in best_by_strategy.items():

        print(f"{result['strategy']}: "
            f"{result['average_time']:.3f}s "
            f"| Risk: {result['variation']:.3f}")

    print("\nBest Strategy:")
    print(optimiser.evaluator.format_strategy(best_strategy))

    print("\nHistorical Data")
    print("Average Lap:", estimator.estimate_average_pace(laps))
    print("Fastest Lap:", estimator.estimate_fastest_lap(laps))
    print("Stints:", estimator.estimate_stint_lengths(laps))

    # monte carlo stuff
    monte_carlo = MonteCarloSimulator()
    result = monte_carlo.simulate(driver,
        track,
        Strategy(
        starting_compound="Medium",
        pit_stops=[
            PitStop(
                lap=25,
                new_compound="Hard",
                pit_time_loss=22.5
            )
        ]
    ),
        iterations=1000,
        verbose=True,
        degradation_rates=degradation)


    print("\nMonte Carlo Results:")
    print(f"Average: {result['average_time']:.3f}s")
    print(f"Best: {result['best_time']:.3f}s")
    print(f"Variation: {result['variation']:.3f}")
    print(f"Consistency Score: {result['consistency_score']:.3f}")