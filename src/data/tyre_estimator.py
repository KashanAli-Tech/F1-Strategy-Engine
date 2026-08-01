import numpy as np

class TyreEstimator:

    def estimate_degradation(self, laps):

        degradation = {}
        compounds = ["SOFT", "MEDIUM", "HARD"]

        for compound in compounds:
            compound_laps = laps[laps["Compound"] == compound].copy()

            if len(compound_laps) < 5:
                continue

            compound_laps["LapSeconds"] = (compound_laps["LapTime"].dt.total_seconds())
            compound_laps = compound_laps.dropna(subset=["LapSeconds"])

            if len(compound_laps) < 15:
                continue

            compound_laps["TyreAge"] = (compound_laps.groupby("Stint").cumcount())
            x = compound_laps["TyreAge"].values
            y = compound_laps["LapSeconds"].values

            # using linear regression to make an accurate estimation
            slope, intercept = np.polyfit(x, y, 1)
            degradation[compound] = max(slope, 0) 

        return degradation