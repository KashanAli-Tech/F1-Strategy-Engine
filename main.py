from src.models.driver import Driver
from src.models.track import Track
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.models.tyre_factory import TyreFactory
from src.strategy.strategy_optimiser import StrategyOptimiser
from src.simulation.monte_carlo import MonteCarloSimulator
from src.data.fastf1_loader import FastF1Loader
from src.data.lap_extractor import LapExtractor
from src.data.parameter_estimator import ParameterEstimator

if __name__ == "__main__":

    driver = Driver(name="Max Verstappen",
        pace=0.98,
        consistency=0.97,
        tyre_management=0.95,)

    track = Track(name="Silverstone",
        number_of_laps=70,
        base_lap_time=90,
        fuel_effect_per_lap=0.035,
        tyre_wear_multiplier=1.15,
        track_evolution_rate=0.01,)

    tyre = TyreFactory.create("Medium")

    optimiser = StrategyOptimiser()
    best_strategy, results = optimiser.optimise(driver, track)
    print("\nBest Pit Window For Each Strategy:\n")

    best_by_strategy = {}
    for strategy, analysis in results.items():

        base_strategy = strategy.split(" (Pit Lap")[0]

        if (base_strategy not in best_by_strategy or analysis["average_time"] < best_by_strategy[base_strategy]["average_time"]):
            best_by_strategy[base_strategy] = {"strategy": strategy,
                "average_time": analysis["average_time"],
                "variation": analysis["variation"]}

    for name, result in best_by_strategy.items():

        print(f"{result['strategy']}: "
              f"{result['average_time']:.3f}s "
              f"| Risk: {result['variation']:.3f}")

    print("\nBest Strategy:")
    print(best_strategy)

    loader = FastF1Loader()

    session = loader.load_race(2024, "British Grand Prix")
    extractor = LapExtractor()
    laps = extractor.extract_driver_laps(session, "VER")
    estimator = ParameterEstimator()

    print()
    print("Historical Data")
    print("----------------")
    print("Average Lap:",
        estimator.estimate_average_pace(laps))

    print("Fastest Lap:",
        estimator.estimate_fastest_lap(laps))

    print("Stints:",
        estimator.estimate_stint_lengths(laps))

    print()

    monte_carlo = MonteCarloSimulator()

    result = monte_carlo.simulate(driver,
        track,
        Strategy(starting_compound="Medium",
            pit_stops=[
                PitStop(
                    lap=25,
                    new_compound="Hard",
                    pit_time_loss=22.5)]),
        iterations=1000, 
        verbose=True)


    print("\nMonte Carlo Results:")
    print(f"Average: {result['average_time']:.3f}s")
    print(f"Best: {result['best_time']:.3f}s")
    print(f"Variation: {result['variation']:.3f}")
    print(f"Consistency Score: {result['consistency_score']:.3f}")