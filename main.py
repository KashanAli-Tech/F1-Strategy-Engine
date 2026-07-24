from src.models.driver import Driver
from src.models.track import Track
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.models.tyre_factory import TyreFactory
from src.strategy.strategy_optimizer import StrategyOptimizer
from src.simulation.monte_carlo import MonteCarloSimulator

if __name__ == "__main__":

    driver = Driver(name="Max Verstappen",
        pace=0.98,
        consistency=0.97,
        tyre_management=0.95,)

    track = Track(name="Silverstone",
        number_of_laps=52,
        base_lap_time=90,
        fuel_effect_per_lap=0.035,
        tyre_wear_multiplier=1.15,)

    tyre = TyreFactory.create("Medium")

    optimizer = StrategyOptimizer()
    best_strategy, results = optimizer.optimise(driver, track)
    print("\nStrategy Results:")

    for strategy, analysis in results.items():

        print(
            f"{strategy}: "
            f"{analysis['average_time']:.3f}s "
            f"| Risk: {analysis['variation']:.3f}"
        )

    print("\nBest Strategy:")
    print(best_strategy)

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