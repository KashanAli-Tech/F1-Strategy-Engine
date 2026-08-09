
import fastf1


# Store downloaded F1 data locally so it does not need
# to be downloaded again.
fastf1.Cache.enable_cache("cache")


class FastF1Loader:

    def load_race(self, year: int, grand_prix: str):
        session = fastf1.get_session(year, grand_prix, "R")
        session.load()
        return session

    def get_schedule(self, year: int):
        return fastf1.get_event_schedule(year)

    def get_grand_prix(self, year: int):
        schedule = self.get_schedule(year)
        races = schedule[schedule["EventName"].notna()]["EventName"].tolist()
        return races

    def get_available_years(self,
        grand_prix: str,
        start_year=2018,
        end_year=2026):
        available_years = []

        for year in range(start_year, end_year + 1):

            try:
                schedule = self.get_schedule(year)

                if grand_prix in schedule["EventName"].values:
                    available_years.append(year)

            except Exception:
                continue

        return available_years

    def get_drivers(self, year: int, grand_prix: str):
        session = self.load_race(year, grand_prix)
        drivers = session.results["Abbreviation"].dropna().unique()
        return sorted(drivers.tolist())

