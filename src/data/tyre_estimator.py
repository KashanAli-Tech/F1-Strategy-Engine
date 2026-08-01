class TyreEstimator:

    def estimate_degradation(self, laps):

        degradation = {}
        compounds = ["SOFT", "MEDIUM", "HARD"]

        for compound in compounds:

            compound_laps = laps[laps["Compound"] == compound]

            if len(compound_laps) < 5:
                continue

            compound_laps = compound_laps.copy()
            compound_laps["LapSeconds"] = (
                compound_laps["LapTime"]
                .dt.total_seconds()
            )

            first_lap = compound_laps["LapSeconds"].iloc[0]

            last_lap = compound_laps["LapSeconds"].iloc[-1]

            lap_numbers = compound_laps["LapNumber"]
            lap_times = compound_laps["LapSeconds"]

            slope = (
                (lap_times.iloc[-1] - lap_times.iloc[0]) /
                (lap_numbers.iloc[-1] - lap_numbers.iloc[0])
            )

            rate = max(slope, 0)

            degradation[compound] = rate

        return degradation