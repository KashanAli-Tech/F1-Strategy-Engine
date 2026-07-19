from dataclasses import dataclass

@dataclass
class Driver:
    # represents a driver

    name: str
    pace: float # overall rating (0-1)
    consistency: float # (0-1)
    tyre_management: float # (0-1)
