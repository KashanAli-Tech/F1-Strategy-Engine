from multiprocessing import Pool, cpu_count

from src.simulation.race_simulator import RaceSimulator
from src.models.tyre_factory import TyreFactory


def run_single_simulation(args):
    # 1 worker
    driver, track, strategy = args
    simulator = RaceSimulator()
    starting_tyre = TyreFactory.create(strategy.starting_compound)
    race_time = simulator.simulate_race(driver, starting_tyre, track, strategy, verbose=False)
    return race_time


class MonteCarloSimulator:

    def simulate(self, driver, track, strategy, iterations=1000, verbose=False):
        workers = cpu_count()
        if verbose:
            print(f"Running {iterations} simulations using {workers} workers")

        simulation_inputs = [(driver, track, strategy) for _ in range(iterations)] # inputs for simulations
        with Pool(workers) as pool:

            # simulates 1000 races and stores finish times as a result
            results = pool.map(run_single_simulation, simulation_inputs) 
        average_time = sum(results) / len(results)
        return {
            "average_time": average_time,
            "best_time": min(results),
            "worst_time": max(results)
        }