from dataclasses import dataclass
from src.models.weather import Weather


@dataclass
class RaceEnvironment:

    weather: Weather
    safety_car_lap: int | None