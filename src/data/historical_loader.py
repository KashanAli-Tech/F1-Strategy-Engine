import pandas as pd

from src.data.fastf1_loader import FastF1Loader
from src.data.lap_extractor import LapExtractor


class HistoricalLoader:

    def __init__(self):
        self.loader = FastF1Loader()
        self.extractor = LapExtractor()

    def load(self, years, race_name, driver):
        all_laps = []

        for year in years:

            print(f"Loading {race_name} {year}")
            session = self.loader.load_race(year, race_name)
            laps, pit_laps = self.extractor.extract_driver_laps(session, driver)
            laps.loc[:, "Year"] = year
            laps["ActualPitLaps"] = [pit_laps] * len(laps)
            all_laps.append(laps)

        combined_laps = pd.concat(all_laps, ignore_index=True)
        return combined_laps