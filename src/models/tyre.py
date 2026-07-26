from dataclasses import dataclass
import random


@dataclass
class Tyre:
   # represents a tyre compound

    compound: str
    base_pace: float
    degradation_rate: float
    cliff_lap: int

    def calculate_degradation(self, tyre_age: int, tyre_management: float) -> float:

        effective_rate = (self.degradation_rate * (2 - tyre_management))
        base_degradation = tyre_age * effective_rate

        if tyre_age > self.cliff_lap:
            base_degradation += ((tyre_age - self.cliff_lap) * self.degradation_rate)

        # the uncertainty in tyre behaviour
        degradation_variation = random.normalvariate(0, 0.05)
        degradation = base_degradation + degradation_variation
        return max(degradation, 0)