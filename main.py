from src.models.driver import Driver
from src.models.track import Track
from src.simulation.race_simulator import RaceSimulator
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.models.tyre_factory import TyreFactory
from src.strategy.strategy_optimizer import StrategyOptimizer
from src.simulation.monte_carlo import MonteCarloSimulator

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

for strategy, time in results.items():
    print(f"{strategy}: {time:.3f}s")

print("\nBest Strategy:")
print(best_strategy)

monte_carlo = MonteCarloSimulator()

result = monte_carlo.simulate(
    driver,
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
    iterations=1000
)


print("\nMonte Carlo Results:")

print(
    f"Average: {result['average_time']:.3f}s"
)

print(
    f"Best: {result['best_time']:.3f}s"
)

print(
    f"Worst: {result['worst_time']:.3f}s"
)