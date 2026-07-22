from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.strategy.strategy_evaluator import StrategyEvaluator
from src.models.driver import Driver
from src.models.track import Track


class StrategyOptimizer:

    def __init__(self):
        self.evaluator = StrategyEvaluator()


    def generate_strategies(self) -> list[Strategy]:
        compounds = ["Soft", "Medium", "Hard"]
        strategies = []

        for start in compounds:
            for next_tyre in compounds:

                # don't create same tyre strategy
                if start == next_tyre:
                    continue

                strategy = Strategy(starting_compound=start,
                    pit_stops=[
                        PitStop(
                            lap=25,
                            new_compound=next_tyre,
                            pit_time_loss=22.5)]
                )

                strategies.append(strategy)

        return strategies


    def optimise(self, driver: Driver, track: Track):
        strategies = self.generate_strategies()
        results = self.evaluator.evaluate(driver, track, strategies)
        best_strategy = min(results, key=results.get)
        return best_strategy, results