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

    def generate_weather_change(self, weather):

        if random.random() >= 0.30:
            return None, None

        change_lap = random.randint(15, 45)

        if weather == Weather.DRY:
            new_weather = random.choice([Weather.LIGHT_RAIN, Weather.HEAVY_RAIN])

        elif weather == Weather.LIGHT_RAIN:
            new_weather = random.choice([Weather.DRY, Weather.HEAVY_RAIN])

        else:
            new_weather = Weather.LIGHT_RAIN

        return change_lap, new_weather

    def generate(self):
        weather = self.generate_weather()
        safety_car_lap = self.generate_safety_car()
        weather_change_lap, new_weather = self.generate_weather_change(weather)

        return RaceEnvironment(weather=weather,
            safety_car_lap=safety_car_lap,
            weather_change_lap=weather_change_lap,
            new_weather=new_weather)