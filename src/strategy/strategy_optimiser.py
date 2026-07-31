from src.strategy.race_strategy import Strategy
from src.strategy.pit_stop import PitStop
from src.strategy.strategy_evaluator import StrategyEvaluator
from src.models.driver import Driver
from src.models.track import Track
from src.strategy.decision_engine import DecisionEngine


class StrategyOptimiser:

    def __init__(self):
        self.evaluator = StrategyEvaluator()
        self.decision_engine = DecisionEngine(risk_factor=1.0)


    def generate_strategies(self, track: Track) -> list[Strategy]:
        compounds = ["Soft", "Medium", "Hard"]
        pit_laps = range(20, track.number_of_laps - 15, 15)   
        strategies = []

        # for one stop strategy
        for start in compounds:
            for next_tyre in compounds:
                if start == next_tyre:
                    continue

                for pit_lap in pit_laps:
                    strategy = Strategy(starting_compound=start,
                                        pit_stops=[
                                        PitStop(lap=pit_lap,
                                        new_compound=next_tyre,
                                        pit_time_loss=22.5)])
                    
                    if self.is_valid_strategy(strategy):
                        strategies.append(strategy)

        # fro two stop strategy
        for start in compounds:
            for tyre2 in compounds:
                if tyre2 == start:
                    continue

                for tyre3 in compounds:
                    if tyre3 == tyre2:
                        continue

                    for pit1 in pit_laps:
                        for pit2 in pit_laps:
                            if pit2 - pit1 < 10:
                                continue

                            
                            strategy = Strategy(starting_compound=start,
                                    pit_stops=[
                                        PitStop(lap=pit1,
                                            new_compound=tyre2,
                                            pit_time_loss=22.5),

                                        PitStop(lap=pit2,
                                            new_compound=tyre3,
                                            pit_time_loss=22.5)])

                            if self.is_valid_strategy(strategy):
                                strategies.append(strategy)

        return strategies

    def optimise(self, driver: Driver, track: Track):
        strategies = self.generate_strategies(track)
        results = self.evaluator.evaluate(driver, track, strategies)
        best_strategy, _ = self.decision_engine.choose_best(results)
        return best_strategy, results

    def is_valid_strategy(self, strategy: Strategy) -> bool:

        previous_lap = 0
        previous_compound = strategy.starting_compound

        for pit in strategy.pit_stops:

            # cannot pit too soon after previous stop
            if pit.lap - previous_lap < 12:
                return False

            # cannot use same compound twice in a row
            if pit.new_compound == previous_compound:
                return False

            previous_lap = pit.lap
            previous_compound = pit.new_compound

        return True