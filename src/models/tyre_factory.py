from src.models.tyre import Tyre


class TyreFactory:

    @staticmethod
    def create(compound: str, degradation_rates=None) -> Tyre:

        default_rates = {
            "Soft": 0.12,
            "Medium": 0.08,
            "Hard": 0.05
        }

        degradation_rate = default_rates[compound]

        if degradation_rates:
            degradation_rate = degradation_rates.get(
                compound.upper(),
                degradation_rate
            )

        tyres = {"Soft": Tyre(compound="Soft",
                base_pace=-0.8,
                degradation_rate=degradation_rate,
                cliff_lap=18),

                "Medium": Tyre(compound="Medium",
                    base_pace=0.0,
                    degradation_rate=degradation_rate,
                    cliff_lap=25),

                "Hard": Tyre(compound="Hard",
                    base_pace=0.5,
                    degradation_rate=degradation_rate,
                    cliff_lap=35)
        }

        return tyres[compound]