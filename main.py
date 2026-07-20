from src.models.driver import Driver
from src.models.track import Track
from src.models.tyre import Tyre
from src.simulation.race_simulator import RaceSimulator


driver = Driver(name="Max Verstappen",
    pace=0.98,
    consistency=0.97,
    tyre_management=0.95,)

track = Track(name="Silverstone",
    number_of_laps=52,
    base_lap_time=90,
    fuel_effect_per_lap=0.035,
    tyre_wear_multiplier=1.15,)

tyre = Tyre(compound="Medium",
    base_pace=0,
    degradation_rate=0.08,
    cliff_lap=25,)

simulator = RaceSimulator()

total_time = simulator.simulate_race(driver,
    tyre,
    track,)

print("\nRace Finished")
print(f"Driver: {driver.name}")
print(f"Total Time: {total_time:.3f}s")