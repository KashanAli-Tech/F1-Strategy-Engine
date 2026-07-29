import random

from src.models.driver import Driver
from src.models.tyre import Tyre
from src.models.track import Track
from src.models.weather import Weather
from configs.simulation_config import LAP_TIME_RANDOMNESS_MULTIPLIER, HEAVY_TRAFFIC, LIGHT_TRAFFIC


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
        track_evolution = (track.number_of_laps - tyre_age) * track.track_evolution_rate
        lap_time = (track.base_lap_time + fuel_effect - track_evolution)
        driver_effect = (1 - driver.pace) * 2 # driver's performance effect
        tyre_effect = tyre.base_pace # tyre compound's starting performance
        degradation = (tyre.calculate_degradation(tyre_age, driver.tyre_management) * track.tyre_wear_multiplier)

        weather_effect = 0

        if environment.weather == Weather.LIGHT_RAIN:

            if tyre.compound == "Soft":
                weather_effect = 1.5

            elif tyre.compound == "Medium":
                weather_effect = 1.0

            elif tyre.compound == "Hard":
                weather_effect = 0.8


        elif environment.weather == Weather.HEAVY_RAIN:

            if tyre.compound == "Soft":
                weather_effect = 5.0

            elif tyre.compound == "Medium":
                weather_effect = 4.0

            elif tyre.compound == "Hard":
                weather_effect = 3.0

        traffic_effect = 0

        # traffic is more likely in the middle of the race so
        race_progress = tyre_age / track.number_of_laps

        if 0.15 < race_progress < 0.85:
            traffic_roll = random.random()

            
            if traffic_roll < LIGHT_TRAFFIC: 
                traffic_effect = random.uniform(0.2, 0.5)

            
            elif traffic_roll < HEAVY_TRAFFIC:
                traffic_effect = random.uniform(0.6, 1.5)

        random_variation = random.normalvariate(0, (1 - driver.consistency) * LAP_TIME_RANDOMNESS_MULTIPLIER)

        total_lap_time = (lap_time
            + driver_effect
            + tyre_effect
            + degradation
            + weather_effect
            + traffic_effect
            + random_variation)

        return total_lap_time