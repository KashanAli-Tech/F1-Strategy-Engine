from dataclasses import dataclass


@dataclass
class Tyre:
   # represents a tyre compound

    compound: str
    base_pace: float
    degradation_rate: float
    cliff_lap: int

    def calculate_degradation(self, tyre_age: int, tyre_management: float) -> float:
      #  calculates total lap time loss caused by tyre wear.

        effective_rate = (self.degradation_rate * (2 - tyre_management))
        degradation = tyre_age * effective_rate
        
        if tyre_age > self.cliff_lap:
            degradation += (tyre_age - self.cliff_lap) * self.degradation_rate

        return degradation