import numpy as np

class Backtester:

    def __init__(self):
        pass


    def calculate_pit_window_error(self, predicted_stops, actual_stops):

        if not predicted_stops or not actual_stops:
            return None

        errors = []

        for predicted in predicted_stops:
            closest = min(actual_stops, key=lambda x: abs(x - predicted))
            errors.append(abs(predicted - closest))

        return round(np.mean(errors),2)

    def calculate_compound_match(self, predicted_compounds, actual_compounds):

        predicted = [c.upper() for c in predicted_compounds]
        actual = [c.upper() for c in actual_compounds]

        matches = sum(1 for compound in predicted if compound in actual)

        return {
            "matches": matches,
            "total": len(actual)
        }
    def extract_actual_pit_laps(self, historical_laps):

        if "ActualPitLaps" not in historical_laps.columns:
            return []

        return historical_laps["ActualPitLaps"].iloc[0]

    def extract_actual_compounds(self, historical_laps):

        if "Compound" not in historical_laps.columns:
            return []

        compounds = (historical_laps["Compound"].dropna().unique().tolist())
        return compounds

    def calculate_actual_variation(self, historical_laps):

        lap_times = historical_laps["LapTime"].dt.total_seconds().dropna()

        if len(lap_times) < 2:
            return 0

        return round(float(lap_times.std()), 3)

    def evaluate(self, strategy, historical_laps, predicted_result):

        predicted_pit_laps = [pit.lap for pit in strategy.pit_stops]
        predicted_compounds = [strategy.starting_compound]

        for pit in strategy.pit_stops:
            predicted_compounds.append(pit.new_compound)

        actual_pit_laps = self.extract_actual_pit_laps(historical_laps)
        actual_compounds = self.extract_actual_compounds(historical_laps)
        pit_window_error = self.calculate_pit_window_error(predicted_pit_laps, actual_pit_laps)
        compound_match = self.calculate_compound_match(predicted_compounds, actual_compounds)

        return {"strategy": strategy,
            "predicted_pit_laps": predicted_pit_laps,
            "actual_pit_laps": actual_pit_laps,
            "pit_window_error": pit_window_error,
            "predicted_compounds": predicted_compounds,
            "actual_compounds": actual_compounds,
            "compound_match": compound_match}