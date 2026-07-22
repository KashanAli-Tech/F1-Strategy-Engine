from src.models.tyre import Tyre


class TyreFactory:

    @staticmethod
    def create(compound: str) -> Tyre:

        tyres = {"Soft": Tyre(compound="Soft",
                base_pace=-0.8,
                degradation_rate=0.12,
                cliff_lap=18),

                "Medium": Tyre(compound="Medium",
                    base_pace=0.0,
                    degradation_rate=0.08,
                    cliff_lap=25),

                "Hard": Tyre(compound="Hard",
                    base_pace=0.5,
                    degradation_rate=0.05,
                    cliff_lap=35)
        }

        return tyres[compound]