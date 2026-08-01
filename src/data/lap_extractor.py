class LapExtractor:

    def extract_driver_laps(self, session, driver):

        laps = session.laps.pick_driver(driver) 
        laps = laps[laps["Compound"].notna()] # this removes laps without tyre compund info
        laps = laps.pick_quicklaps() # this removes slow laps
        return laps