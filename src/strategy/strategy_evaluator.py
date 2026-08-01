from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre_factory import TyreFactory
from src.strategy.race_strategy import Strategy
from src.simulation.monte_carlo import MonteCarloSimulator


class StrategyEvaluator:

    def __init__(self, degradation_rates=None):
        self.simulator = MonteCarloSimulator()
        self.degradation_rates = degradation_rates

    def evaluate(self, driver: Driver, track: Track, strategies: list[Strategy], iterations=200) -> list:

        results = []

        for strategy in strategies:

            result = self.simulator.simulate(
                driver,
                track,
                strategy,
                iterations=iterations,
                degradation_rates=self.degradation_rates
            )

            results.append((strategy, result))

        return results


    def find_best_strategy(self, results: dict):
        return min(results, key=lambda strategy: results[strategy]["average_time"])


    def format_strategy(self, strategy: Strategy) -> str:
        name = strategy.starting_compound

        for pit in strategy.pit_stops:

            name += f" → {pit.new_compound}"

        laps = ", ".join(str(pit.lap) for pit in strategy.pit_stops)
        return f"{name} (Pit Laps {laps})"