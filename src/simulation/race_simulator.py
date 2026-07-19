from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre import Tyre
from src.simulation.lap_simulator import LapSimulator


class RaceSimulator:
    # simulates a complete race
    
    def __init__(self):
        self.lap_simulator = LapSimulator()

    def simulate_race(self,
        driver: Driver,
        tyre: Tyre,
        track: Track,) -> float:

        total_time = 0.0 
        tyre_age = 0

        for lap in range(1, track.number_of_laps + 1):

            lap_time = self.lap_simulator.simulate_lap(driver,
                tyre,
                track,
                tyre_age,)

            total_time += lap_time
            tyre_age += 1

            print(f"Lap {lap}: "
                f"{lap_time:.3f}s | "
                f"Tyre Age: {tyre_age}")

        return total_time