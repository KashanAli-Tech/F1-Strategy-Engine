from dataclasses import dataclass

@dataclass
class RaceState:
# represents the current state of a race
    current_lap: int
    driver_position: dict
    tyre_age: dict
    weather: str