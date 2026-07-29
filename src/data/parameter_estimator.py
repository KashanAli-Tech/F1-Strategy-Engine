class ParameterEstimator:

    def estimate_average_pace(self, laps):
        return laps["LapTime"].dt.total_seconds().mean()

    def estimate_fastest_lap(self, laps):
        return laps["LapTime"].dt.total_seconds().min()

    def estimate_stint_lengths(self, laps):
        return laps.groupby("Stint").size().tolist()