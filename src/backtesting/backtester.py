class Backtester:

    def __init__(self, historical_loader, simulator, optimizer):
        self.loader = historical_loader
        self.simulator = simulator
        self.optimizer = optimizer


    def run_race(self, year, event):

        print(f"Backtesting {event} {year}")
        laps = self.loader.load(year=year, event=event)
        strategies = self.optimizer.generate_strategies()
        results = {}

        for strategy in strategies:

            simulation = self.simulator.simulate_strategy(strategy, laps)
            results[str(strategy)] = simulation

        return results