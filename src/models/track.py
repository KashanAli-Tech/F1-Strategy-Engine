from dataclasses import dataclass

@dataclass
class Track:
    # represents a F1 circuit

    name: str
    number_of_laps: int
    base_lap_time: float
    fuel_effect_per_lap: float
    tyre_wear_multiplier: float