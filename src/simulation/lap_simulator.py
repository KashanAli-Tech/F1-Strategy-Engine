import random

from src.models.driver import Driver
from src.models.tyre import Tyre
from src.models.track import Track
from src.models.weather import Weather


class LapSimulator:
    # simulates a single lap of a race
    

    def simulate_lap(self,
        driver: Driver,
        tyre: Tyre,
        track: Track,
        tyre_age: int, 
        environment) -> float:
        # calculates lap time

        fuel_effect = (track.number_of_laps - tyre_age) * track.fuel_effect_per_lap
        lap_time = track.base_lap_time + fuel_effect
        driver_effect = (1 - driver.pace) * 2 # driver's performance effect
        tyre_effect = tyre.base_pace # tyre compound's starting performance
        degradation = (tyre.calculate_degradation(tyre_age, driver.tyre_management) * track.tyre_wear_multiplier)

        weather_effect = 0

        weather_effect = 0

        if environment.weather == Weather.LIGHT_RAIN:
            if random.random() < 0.3:
                weather_effect = 0.3


        elif environment.weather == Weather.HEAVY_RAIN:
            if random.random() < 0.7:
                weather_effect = 0.8

        random_variation = random.normalvariate(0, (1 - driver.consistency) * 1.5)

        total_lap_time = (lap_time
            + driver_effect
            + tyre_effect
            + degradation
            + weather_effect
            + random_variation)

        return total_lap_time