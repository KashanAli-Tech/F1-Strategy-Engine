class ParameterEstimator:

    def estimate_average_pace(self, laps):
        return laps["LapTime"].dt.total_seconds().mean()

    def estimate_fastest_lap(self, laps):
        return laps["LapTime"].dt.total_seconds().min()

    def estimate_stint_lengths(self, laps):
        return (laps.dropna(subset=["Year", "Driver", "Stint", "LapNumber"])
            .groupby(["Year", "Driver", "Stint"])["LapNumber"]
            .agg(first_lap="min", last_lap="max", rows="size")
            .assign(length=lambda df: df["last_lap"] - df["first_lap"] + 1)
            .reset_index())