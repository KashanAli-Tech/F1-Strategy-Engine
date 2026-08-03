class LapExtractor:

    def extract_driver_laps(self, session, driver):

        laps = session.laps.pick_drivers(driver).copy()
        actual_pit_laps = (laps[laps["PitInTime"].notna()]["LapNumber"].tolist())
        laps = laps[laps["Compound"].notna()].copy()
        laps = laps.pick_quicklaps().copy()
        laps["TyreAge"] = (laps.groupby("Stint").cumcount())
        return laps, actual_pit_laps