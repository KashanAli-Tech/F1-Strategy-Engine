from dataclasses import dataclass
import random


@dataclass
class Tyre:
   # represents a tyre compound

    compound: str
    base_pace: float
    degradation_rate: float
    cliff_lap: int

    def calculate_degradation(self, tyre_age, driver_management):
        base_wear = self.degradation_rate * tyre_age

        # driver tyre management reduces wear
        management_factor = 1 - (driver_management * 0.2)
        degradation = base_wear * management_factor
        
        # tyre cliff
        if tyre_age > self.cliff_lap:
            cliff_factor = (tyre_age - self.cliff_lap) ** 1.5
            degradation += cliff_factor * 0.05

        return degradation