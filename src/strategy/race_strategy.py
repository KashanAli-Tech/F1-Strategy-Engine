from dataclasses import dataclass


@dataclass
class Strategy:
    # represents a race strategy
    

    starting_compound: str
    pit_laps: list[int]
    compounds: list[str]