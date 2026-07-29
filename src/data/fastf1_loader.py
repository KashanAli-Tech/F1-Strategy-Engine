import fastf1

# this stores downloaded F1 data locally so it doesn't need to download it again
fastf1.Cache.enable_cache("cache")

class FastF1Loader:

    def load_race(self, year: int, grand_prix: str):
        session = fastf1.get_session(year, grand_prix, "R")
        session.load()
        return session