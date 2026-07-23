from dataclasses import dataclass

@dataclass
class RaceEnvironment:
    weather: str
    safety_car_lap: int | None