import numpy as np


class TyreEstimator:

    def estimate_degradation(self, laps):
        degradation_rates = {}

        for compound in laps["Compound"].unique():

            tyre_laps = laps[laps["Compound"] == compound]

            if len(tyre_laps) < 5:
                continue

            lap_times = (tyre_laps["LapTime"].dt.total_seconds().values)
            lap_numbers = np.arange(len(lap_times))
            slope, _ = np.polyfit(lap_numbers, lap_times, 1)
            degradation_rates[compound] = slope

        return degradation_rates