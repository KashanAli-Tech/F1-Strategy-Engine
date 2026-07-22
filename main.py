from src.models.driver import Driver
from src.models.track import Track
from src.simulation.race_simulator import RaceSimulator
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.models.tyre_factory import TyreFactory
from src.strategy.strategy_evaluator import StrategyEvaluator

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

strategies = [

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

    Strategy(
        starting_compound="Soft",
        pit_stops=[
            PitStop(
                lap=20,
                new_compound="Medium",
                pit_time_loss=22.5
            )
        ]
    )
]

evaluator = StrategyEvaluator()

results = evaluator.evaluate(
    driver,
    track,
    strategies
)

print("\nStrategy Results:")

for strategy, time in results.items():
    print(f"{strategy}: {time:.3f}s")

best = evaluator.find_best_strategy(results)

print("\nBest Strategy:")
print(best)

print("\nRace Finished")
print(f"Driver: {driver.name}")
