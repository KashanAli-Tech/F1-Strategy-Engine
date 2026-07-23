import random

from src.models.race_environment import RaceEnvironment

class EnvironmentGenerator:

    def generate(self):
        weather_roll = random.random()

        if weather_roll < 0.7:
            weather = "Dry"

        elif weather_roll < 0.9:
            weather = "Light Rain"

        else:
            weather = "Heavy Rain"

        safety_car_lap = None

        if random.random() < 0.25:
            safety_car_lap = random.randint(10, 45)

        return RaceEnvironment(weather=weather, safety_car_lap=safety_car_lap)