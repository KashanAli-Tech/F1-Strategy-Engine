from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre import Tyre
from src.simulation.lap_simulator import LapSimulator
from src.strategy.race_strategy import Strategy

class RaceSimulator:
    # simulates a complete race
    
    def __init__(self):
        self.lap_simulator = LapSimulator()

    def simulate_race(self, driver: Driver, tyre: Tyre, track: Track, strategy: Strategy,) -> float:

        total_time = 0.0 
        tyre_age = 0
        current_compound = tyre
        for lap in range(1, track.number_of_laps + 1):

            # to check if pit stop happens this lap
            for pit_stop in strategy.pit_stops:
                if lap == pit_stop.lap:
                    print(
                            f"\nPIT STOP LAP {lap}: "
                            f"Changing to {pit_stop.new_compound}"
                        )

                    total_time += pit_stop.pit_time_loss

                    current_compound = Tyre(compound=pit_stop.new_compound, base_pace=0, degradation_rate=0.08, cliff_lap=25)

                tyre_age = 0

            lap_time = self.lap_simulator.simulate_lap(driver, current_compound, track, tyre_age,)

            total_time += lap_time
            tyre_age += 1

            print(
                f"Lap {lap}: "
                f"{lap_time:.3f}s | "
                f"Tyre Age: {tyre_age}"
            )

        return total_time