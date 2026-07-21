from dataclasses import dataclass


@dataclass
class PitStop:
    # represents a pit stop during a race

    lap: int
    new_compound: str
    pit_time_loss: float