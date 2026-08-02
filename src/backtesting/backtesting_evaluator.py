class BackTestedStrategyEvaluator:


    def evaluate(self, results):

        best_prediction = min(results, key=lambda x:x["predicted"]) 
        closest_actual = min(results,key=lambda x:x["error"])
        return {"predicted_strategy": best_prediction["strategy"],
            "actual_closest": closest_actual["strategy"],
            "error": best_prediction["error"]}