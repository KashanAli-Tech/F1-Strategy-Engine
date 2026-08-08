import fastf1

def get_races(year):
    schedule = fastf1.get_event_schedule(year)
    return schedule["EventName"].tolist()

def get_available_years(race_name, start=2022, end=2024):
    available = []

    for year in range(start, end + 1):
        schedule = fastf1.get_event_schedule(year)

        if race_name in schedule["EventName"].values:
            available.append(year)

    return available

def get_drivers(year, race_name):
    session = fastf1.get_session(year, race_name, "R")
    session.load(laps=False, telemetry=False, weather=False)
    drivers = session.results

    return {row["FullName"]: row["Abbreviation"]
        for _, row in drivers.iterrows()}