from src.models.driver import Driver
from src.models.tyre import Tyre
from src.models.track import Track


class LapSimulator:
    # simulates a single lap of a race
    

    def simulate_lap(self,
        driver: Driver,
        tyre: Tyre,
        track: Track,
        tyre_age: int) -> float:
        # calculates lap time

        fuel_effect = (track.number_of_laps - tyre_age) * track.fuel_effect_per_lap
        lap_time = track.base_lap_time + fuel_effect
        driver_effect = (1 - driver.pace) * 2 # driver's performance effect
        tyre_effect = tyre.base_pace # tyre compound's starting performance
        degradation = tyre.calculate_degradation(tyre_age)

        total_lap_time = (lap_time
            + driver_effect
            + tyre_effect
            + degradation)

        return total_lap_time