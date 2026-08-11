import fastf1#
from configs.dashboard_config import CURRENT_DRIVERS


def get_races(year):

    try:
        schedule = fastf1.get_event_schedule(year)
        return schedule["EventName"].dropna().tolist()

    except Exception:
        return []


def get_available_years(race_name, start=2022, end=2026):
    available = []

    for year in range(start, end + 1):
        try:
            schedule = fastf1.get_event_schedule(year)

            if race_name in schedule["EventName"].values:
                available.append(year)

        except Exception:
            continue

    return available


def get_drivers(year, race_name):
 
    try:
        session = fastf1.get_session(year, race_name, "R")
        session.load(laps=False, telemetry=False, weather=False)
        drivers = session.results

        if drivers is not None and not drivers.empty:

            return {row["FullName"]: row["Abbreviation"] for _, row in drivers.iterrows() if row["FullName"] and row["Abbreviation"]}

    except Exception:
        pass

    if year == 2026:
        return CURRENT_DRIVERS

    for fallback_year in range(year - 1, 2021, -1):
        try:

            session = fastf1.get_session(fallback_year, race_name, "R")
            session.load(laps=False, telemetry=False, weather=False)
            drivers = session.results

            if drivers is not None and not drivers.empty:

                return {row["FullName"]: row["Abbreviation"] for _, row in drivers.iterrows() if row["FullName"] and row["Abbreviation"]}

        except Exception:
            continue

    return {}