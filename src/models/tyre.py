from dataclasses import dataclass


@dataclass
class Tyre:
   # represents a tyre compound

    compound: str
    base_pace: float
    degradation_rate: float
    cliff_lap: int

    def calculate_degradation(self, tyre_age: int) -> float:
      #  calculates total lap time loss caused by tyre wear.

        degradation = tyre_age * self.degradation_rate

        if tyre_age > self.cliff_lap:
            degradation += (tyre_age - self.cliff_lap) * self.degradation_rate

        return degradation