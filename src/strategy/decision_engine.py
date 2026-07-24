class DecisionEngine:

    def __init__(self, risk_factor=1.0):
        self.risk_factor = risk_factor

    def calculate_score(self, analysis):
        # calculates strategy score

        average_time = analysis["average_time"]
        variation = analysis["variation"]
        score = (average_time + (variation * self.risk_factor))
        return score


    def choose_best(self, strategies):
        best_strategy = None
        best_score = float("inf")

        for strategy, analysis in strategies.items():
            score = self.calculate_score(analysis)

            if score < best_score:
                best_score = score
                best_strategy = strategy

        return best_strategy, best_score