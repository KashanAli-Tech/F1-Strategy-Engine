class LapExtractor:

    def extract_driver_laps(self, session, driver):

        laps = session.laps.pick_drivers(driver)
        laps = laps.pick_quicklaps()
        return laps