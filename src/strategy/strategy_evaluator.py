from src.simulation.race_simulator import RaceSimulator
from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre_factory import TyreFactory
from src.strategy.race_strategy import Strategy


class StrategyEvaluator:

    def __init__(self):
        self.simulator = RaceSimulator()

    def evaluate(self, driver: Driver, track: Track, strategies: list[Strategy]) -> dict:
        results = {}

        for strategy in strategies:

            starting_tyre = TyreFactory.create(strategy.starting_compound)
            total_time = self.simulator.simulate_race(driver, starting_tyre, track,strategy, verbose=False)
            strategy_name = self.format_strategy(strategy)
            results[strategy_name] = total_time

        return results


    def find_best_strategy(self,results: dict):
        return min(results, key=results.get)


    def format_strategy(self, strategy: Strategy) -> str:
        name = strategy.starting_compound

        for pit in strategy.pit_stops:
            name += f" → {pit.new_compound}"

        return name