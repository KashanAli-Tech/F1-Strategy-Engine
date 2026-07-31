class ParameterCalibrator:

    def calibrate_track(self, track, estimator, laps):
        track.base_lap_time = estimator.estimate_average_pace(laps)
        stints = estimator.estimate_stint_lengths(laps)

        if len(stints) > 1:
            track.typical_stint = sum(stints) / len(stints)

        return track