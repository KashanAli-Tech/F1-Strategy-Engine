from src.models.driver import Driver
from src.models.track import Track
from src.simulation.race_simulator import RaceSimulator
from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.models.tyre_factory import TyreFactory
from src.strategy.strategy_evaluator import StrategyEvaluator
from src.strategy.strategy_optimizer import StrategyOptimizer

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