import random

from src.models.weather import Weather


class WeatherModel:

    TRANSITIONS = {

        Weather.DRY: {
            Weather.DRY: 0.85,
            Weather.LIGHT_RAIN: 0.13,
            Weather.HEAVY_RAIN: 0.02
        },

        Weather.LIGHT_RAIN: {
            Weather.DRY: 0.20,
            Weather.LIGHT_RAIN: 0.60,
            Weather.HEAVY_RAIN: 0.20
        },

        Weather.HEAVY_RAIN: {
            Weather.DRY: 0.05,
            Weather.LIGHT_RAIN: 0.35,
            Weather.HEAVY_RAIN: 0.60
        }
    }


    def next_weather(self, current_weather):

        roll = random.random()
        cumulative = 0

        for weather, probability in self.TRANSITIONS[current_weather].items():

            cumulative += probability

            if roll <= cumulative:
                return weather