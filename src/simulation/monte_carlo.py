from multiprocessing import Pool, cpu_count

from src.simulation.race_simulator import RaceSimulator
from src.models.tyre_factory import TyreFactory
from src.analysis.risk_analyser import RiskAnalyser
from src.simulation.environment_generator import EnvironmentGenerator
from configs.simulation_config import DEFAULT_SIMULATIONS


def run_single_simulation(args):
    driver, track, strategy, degradation_rates = args
    environment_generator = EnvironmentGenerator()
    environment = environment_generator.generate()
    simulator = RaceSimulator()
    starting_tyre = TyreFactory.create(strategy.starting_compound, degradation_rates)
    race_time = simulator.simulate_race(driver, starting_tyre, track, strategy, environment, verbose=False)
    return race_time


class MonteCarloSimulator:

    def simulate(self, driver, track, strategy, iterations=DEFAULT_SIMULATIONS, verbose=False, degradation_rates=None):

        workers = cpu_count()
        if verbose:
            print(f"Running {iterations} simulations using {workers} workers")

        simulation_inputs = [(driver, track, strategy, degradation_rates) for _ in range(iterations)]

        with Pool(workers) as pool:

            results = pool.map(run_single_simulation, simulation_inputs)

        risk_analyser = RiskAnalyser()
        analysis = risk_analyser.analyse(results)
        return analysis