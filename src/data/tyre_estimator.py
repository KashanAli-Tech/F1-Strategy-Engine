import numpy as np

class TyreEstimator:

    def estimate_degradation(self, laps):

        degradation = {}
        compounds = ["SOFT", "MEDIUM", "HARD"]

        for compound in compounds:
            compound_laps = laps[laps["Compound"] == compound].copy()

            if len(compound_laps) < 10:
                continue

            compound_laps["LapSeconds"] = (compound_laps["LapTime"].dt.total_seconds())
            compound_laps = compound_laps.dropna(subset=["LapSeconds"])
            slopes = []

            # this calculate degradation per stint
            for _, data in compound_laps.groupby("Stint"):
                if len(data) < 5:
                    continue

                data = data.copy()
                data["TyreAge"] = range(len(data))
                x = data["TyreAge"].values
                y = data["LapSeconds"].values
                slope, _ = np.polyfit(x, y, 1)
                slopes.append(slope)

            if slopes:

                # using this averages only realistic degradation
                degradation[compound] = round(float(np.clip(np.mean(slopes), 0.005, 0.12)), 4)

        return degradation