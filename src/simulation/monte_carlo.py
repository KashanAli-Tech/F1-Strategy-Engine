from multiprocessing import Pool, cpu_count

from src.simulation.race_simulator import RaceSimulator
from src.models.tyre_factory import TyreFactory
from src.analysis.risk_analyser import RiskAnalyser
from src.simulation.environment_generator import EnvironmentGenerator


def run_single_simulation(args):
    # 1 worker
    driver, track, strategy = args
    environment_generator = EnvironmentGenerator()
    environment = environment_generator.generate()
    simulator = RaceSimulator()
    starting_tyre = TyreFactory.create(strategy.starting_compound)
    race_time = simulator.simulate_race(driver, starting_tyre, track, strategy, environment, verbose=False)
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

        risk_analyzer = RiskAnalyser()
        analysis = risk_analyzer.analyse(results)
        return analysis