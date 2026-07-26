import random

from src.models.race_environment import RaceEnvironment
from src.models.weather import Weather

class EnvironmentGenerator:

    WEATHER_PROBABILITIES = {Weather.DRY: 0.7,
        Weather.LIGHT_RAIN: 0.25,
        Weather.HEAVY_RAIN: 0.05}


    def generate_weather(self):
        roll = random.random()
        cumulative = 0

        for weather, probability in self.WEATHER_PROBABILITIES.items():
            cumulative += probability

            if roll <= cumulative:
                return weather

    def generate_safety_car(self):

        if random.random() < 0.25:
            return random.randint(10, 45)

        return None
    
    def generate(self):
        weather = self.generate_weather()
        safety_car_lap = self.generate_safety_car()

        return RaceEnvironment(weather=weather, safety_car_lap=safety_car_lap)