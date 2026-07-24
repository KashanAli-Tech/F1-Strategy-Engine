import random

from src.models.race_environment import RaceEnvironment
from src.models.weather import Weather

class EnvironmentGenerator:

    def generate(self):
        weather_roll = random.random()

        if weather_roll < 0.7:
            weather = Weather.DRY

        elif weather_roll < 0.9:
            weather = Weather.LIGHT_RAIN

        else:
            weather = Weather.HEAVY_RAIN

        safety_car_lap = None

        if random.random() < 0.25:
            safety_car_lap = random.randint(10, 45)

        return RaceEnvironment(weather=weather, safety_car_lap=safety_car_lap)