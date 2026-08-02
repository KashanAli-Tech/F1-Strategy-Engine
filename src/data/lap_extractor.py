class LapExtractor:

    def extract_driver_laps(self, session, driver):

        laps = session.laps.pick_drivers(driver) 
        laps = laps[laps["Compound"].notna()].copy() # this removes laps without tyre compund info
        laps = laps.pick_quicklaps() # this removes slow laps
        laps = laps.copy()
        laps["TyreAge"] = (laps.groupby("Stint").cumcount())
        return laps