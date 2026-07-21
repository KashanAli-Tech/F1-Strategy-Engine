from dataclasses import dataclass
from src.strategy.pit_stop import PitStop

@dataclass
class Strategy:
    # represents a race strategy
    
    starting_compound: str
    pit_stops: list[PitStop]