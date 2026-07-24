from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.strategy.strategy_evaluator import StrategyEvaluator
from src.models.driver import Driver
from src.models.track import Track
from src.strategy.decision_engine import DecisionEngine


class StrategyOptimizer:

    def __init__(self):
        self.evaluator = StrategyEvaluator()
        self.decision_engine = DecisionEngine(risk_factor=1.0)


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
        best_strategy, score = self.decision_engine.choose_best(results)
        return best_strategy, results