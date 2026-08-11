
import pandas as pd

from src.data.fastf1_loader import FastF1Loader
from src.data.lap_extractor import LapExtractor


class HistoricalLoader:

    def __init__(self):
        self.loader = FastF1Loader()
        self.extractor = LapExtractor()

    def load(self, years, race_name, driver):
        all_laps = []
        total_laps = 0

        for year in years:

            print(f"Loading {race_name} {year}")
            session = self.loader.load_race(year, race_name)
            laps, pit_laps = self.extractor.extract_driver_laps(session, driver)

            if laps.empty:
                continue

            laps.loc[:, "Year"] = year
            laps["ActualPitLaps"] = [pit_laps] * len(laps)

            all_laps.append(laps)
            total_laps += len(laps)

        if not all_laps:
            raise ValueError(f"{driver} does not have enough historical data "
                f"for {race_name} to run the strategy engine. "
                f"Select a driver with available historical data.")

        if total_laps < 20:
            raise ValueError(f"{driver} does not have enough historical data "
                f"for {race_name}. Only {total_laps} usable laps "
                f"were found, but at least 20 are required.")

        combined_laps = pd.concat(all_laps, ignore_index=True)

        return combined_laps
