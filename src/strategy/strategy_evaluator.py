from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre_factory import TyreFactory
from src.strategy.race_strategy import Strategy
from src.simulation.monte_carlo import MonteCarloSimulator


class StrategyEvaluator:

    def __init__(self):
        self.simulator = MonteCarloSimulator()

    def evaluate(self, driver: Driver, track: Track, strategies: list[Strategy]) -> dict:
        results = {}

        for strategy in strategies:

            starting_tyre = TyreFactory.create(strategy.starting_compound)
            result = self.simulator.simulate(driver, track, strategy, iterations=1000)
            strategy_name = self.format_strategy(strategy)
            results[strategy_name] = result
        return results


    def find_best_strategy(self, results: dict):
        return min(results, key=lambda strategy: results[strategy]["average_time"])


    def format_strategy(self, strategy: Strategy) -> str:
        name = strategy.starting_compound

        for pit in strategy.pit_stops:
            name += f" → {pit.new_compound}"

        return name