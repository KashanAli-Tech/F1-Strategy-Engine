import random

from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre import Tyre
from src.simulation.lap_simulator import LapSimulator
from src.strategy.race_strategy import Strategy
from src.models.tyre_factory import TyreFactory
from src.models.weather_model import WeatherModel
from configs.simulation_config import PIT_STOP_STD, WEATHER_CHANGE_PROBABILITY, SAFETY_CAR_TIME_LOSS

class RaceSimulator:
    # simulates a complete race
    
    def __init__(self):
        self.lap_simulator = LapSimulator()
        self.weather_model = WeatherModel()

    def simulate_race(self, driver: Driver, tyre: Tyre, track: Track, strategy: Strategy, environment, verbose: bool = True) -> float:

        total_time = 0.0 
        tyre_age = 0
        current_compound = tyre
        current_weather = environment.weather
        for lap in range(1, track.number_of_laps + 1):

            # to check if pit stop happens this lap
            for pit_stop in strategy.pit_stops:
                if lap == pit_stop.lap:
                    if verbose:
                        print(f"\nPIT STOP LAP {lap}: "
                              f"Changing to {pit_stop.new_compound}")

                    pit_time = random.normalvariate(pit_stop.pit_time_loss, PIT_STOP_STD)
                    total_time += pit_time
                    current_compound = TyreFactory.create(pit_stop.new_compound)
                    tyre_age = 0

            if random.random() < WEATHER_CHANGE_PROBABILITY:
                current_weather = self.weather_model.next_weather(current_weather)

                if verbose:
                    print(f"\nWEATHER CHANGED TO {current_weather}")

            environment.weather = current_weather        

            lap_time = self.lap_simulator.simulate_lap(driver, current_compound, track, tyre_age, environment)

            if environment.safety_car_lap == lap:
                if verbose:
                    print("SAFETY CAR DEPLOYED")
                lap_time += SAFETY_CAR_TIME_LOSS

            total_time += lap_time
            tyre_age += 1

            if verbose:
                print(
                    f"Lap {lap}: "
                    f"{lap_time:.3f}s | "
                    f"Tyre Age: {tyre_age}"
                )

        return total_time