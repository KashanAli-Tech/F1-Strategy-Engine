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

        weather_change_lap = None
        new_weather = None

        if random.random() < 0.30:
            weather_change_lap = random.randint(15, 45)

            if weather == Weather.DRY:
                new_weather = random.choice([Weather.LIGHT_RAIN, Weather.HEAVY_RAIN])

            elif weather == Weather.LIGHT_RAIN:
                new_weather = random.choice([Weather.DRY, Weather.HEAVY_RAIN])

            else:  
                new_weather = Weather.LIGHT_RAIN

        return RaceEnvironment(weather=weather,
            safety_car_lap=safety_car_lap,
            weather_change_lap=weather_change_lap,
            new_weather=new_weather,)