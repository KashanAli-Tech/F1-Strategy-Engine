import random

from src.models.race_environment import RaceEnvironment
from src.models.weather import Weather
from configs.simulation_config import SAFETY_CAR_PROBABILITY, SAFETY_CAR_MIN_LAP, SAFETY_CAR_MAX_LAP, INITIAL_WEATHER_PROBABILITIES, WEATHER_CHANGE_PROBABILITY

class EnvironmentGenerator:

    def generate_weather(self):
        roll = random.random()
        cumulative = 0

        for weather, probability in INITIAL_WEATHER_PROBABILITIES.items():
            cumulative += probability

            if roll <= cumulative:
                return weather

    def generate_safety_car(self):

        if random.random() < SAFETY_CAR_PROBABILITY:
            return random.randint(SAFETY_CAR_MIN_LAP, SAFETY_CAR_MAX_LAP)

        return None
    
    def generate(self):
        weather = self.generate_weather()
        safety_car_lap = self.generate_safety_car()

        return RaceEnvironment(weather=weather, safety_car_lap=safety_car_lap)