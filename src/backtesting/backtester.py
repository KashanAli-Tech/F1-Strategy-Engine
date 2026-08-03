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

    def calculate_compound_accuracy(self, predicted_compounds, actual_compounds):

        predicted = set(compound.upper() for compound in predicted_compounds)
        actual = set(compound.upper() for compound in actual_compounds)

        if len(predicted) == 0:
            return 0

        matches = predicted.intersection(actual)
        return round(len(matches) / len(predicted) * 100, 2)

    def extract_actual_pit_laps(self, historical_laps):

        if "PitInTime" not in historical_laps.columns:
            return []

        pit_laps = historical_laps[historical_laps["PitInTime"].notna()]["LapNumber"].tolist()
        return pit_laps

    def extract_actual_compounds(self, historical_laps):

        if "Compound" not in historical_laps.columns:
            return []

        compounds = (historical_laps["Compound"].dropna().unique().tolist())
        return compounds

    def calculate_actual_variation(self, historical_laps):

        if "LapTimeSeconds" not in historical_laps.columns:
            return 0

        return round(historical_laps["LapTimeSeconds"].std(), 3)

    def evaluate(self, strategy, historical_laps, predicted_result):

        predicted_pit_laps = [pit.lap for pit in strategy.pit_stops]
        predicted_compounds = [strategy.starting_compound]

        for pit in strategy.pit_stops:
            predicted_compounds.append(pit.new_compound)

        actual_pit_laps = self.extract_actual_pit_laps(historical_laps)
        actual_compounds = self.extract_actual_compounds(historical_laps)
        pit_window_error = self.calculate_pit_window_error(predicted_pit_laps, actual_pit_laps)
        compound_accuracy = self.calculate_compound_accuracy(predicted_compounds, actual_compounds)
        actual_variation = self.calculate_actual_variation(historical_laps)
        predicted_time = predicted_result["average_time"]

        # keep current placeholder
        actual_time = historical_laps["LapTime"].dt.total_seconds().sum()

        return {"strategy": strategy,
            "predicted_time": predicted_time,
            "actual_time": actual_time,
            "time_error": abs(predicted_time - actual_time),
            "predicted_pit_laps": predicted_pit_laps,
            "actual_pit_laps": actual_pit_laps,
            "pit_window_error": pit_window_error,
            "predicted_compounds": predicted_compounds,
            "actual_compounds": actual_compounds,
            "compound_accuracy": compound_accuracy,
            "predicted_variation": predicted_result["variation"],
            "actual_variation": actual_variation}