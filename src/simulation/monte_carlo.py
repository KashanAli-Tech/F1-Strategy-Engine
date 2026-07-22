from src.simulation.race_simulator import RaceSimulator
from src.models.tyre_factory import TyreFactory


class MonteCarloSimulator:

    def __init__(self):
        self.race_simulator = RaceSimulator()


    def simulate(self, driver, track, strategy, iterations=1000):
        results = []

        for _ in range(iterations):

            starting_tyre = TyreFactory.create(strategy.starting_compound)
            race_time = self.race_simulator.simulate_race(driver,
                starting_tyre,
                track,
                strategy,
                verbose=False)

            results.append(race_time)

        average_time = sum(results) / len(results)
        return {
            "average_time": average_time,
            "best_time": min(results),
            "worst_time": max(results)
        }