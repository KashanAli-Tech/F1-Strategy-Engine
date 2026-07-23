import statistics


class RiskAnalyser:

    def analyse(self, results):
        average_time = sum(results) / len(results)
        best_time = min(results)
        worst_time = max(results)
        variation = statistics.stdev(results)
        consistency_score = 1 / (1 + variation)

        return {
            "average_time": average_time,
            "best_time": best_time,
            "worst_time": worst_time,
            "variation": variation,
            "consistency_score": consistency_score
        }