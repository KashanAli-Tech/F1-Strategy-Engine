import numpy as np

class TyreEstimator:

    def estimate_degradation(self, laps):

        degradation = {}
        compounds = ["SOFT", "MEDIUM", "HARD"]

        for compound in compounds:
            compound_laps = laps[laps["Compound"].str.upper() == compound].copy()

            if len(compound_laps) < 10:
                continue

            compound_laps["LapSeconds"] = (compound_laps["LapTime"].dt.total_seconds())
            compound_laps = compound_laps.dropna(subset=["LapSeconds"])
            slopes = []

            for _, stint in compound_laps.groupby("Stint"):
                if len(stint) < 5:
                    continue

                stint = stint.copy()

                # Remove the first lap of a stint because out-laps are often significantly slower.
                if len(stint) > 6:
                    stint = stint.iloc[1:]

                stint["TyreAge"] = np.arange(len(stint))

                x = stint["TyreAge"].to_numpy()
                y = stint["LapSeconds"].to_numpy()

                # Remove obvious lap-time outliers
                median = np.median(y)
                mad = np.median(np.abs(y - median))

                if mad > 0:
                    mask = np.abs(y - median) < 3 * mad
                    x = x[mask]
                    y = y[mask]

                if len(x) < 5:
                    continue

                slope, _ = np.polyfit(x, y, 1)

                # Ignore slopes which imply tyres getting faster as they age.
                if slope > 0:
                    slopes.append(float(slope))

            if slopes:

                degradation[compound] = round(float(np.median(slopes)), 4)

        return degradation