# 🏎️ F1 Strategy Engine

A probabilistic Formula 1 race strategy optimisation engine that uses Monte Carlo simulation, uncertainty modelling, and optimisation algorithms to evaluate thousands of race scenarios and identify optimal strategies.
The system models tyre degradation, driver performance, pit strategies, and race conditions to simulate possible outcomes and make risk-aware strategy decisions rather than relying on a single deterministic prediction.
Built using Python, the project explores simulation engineering, quantitative modelling, and decision systems with the long-term goal of integrating real F1 data and machine learning techniques.

---

## Features

### Race Simulation
- Lap-by-lap race simulation
- Driver performance modelling
- Fuel effects
- Tyre degradation
- Pit stop simulation

### Tyre & Strategy Modelling
- Soft, Medium, and Hard tyre compounds
- Different tyre degradation behaviours
- Strategy generation and evaluation
- Variable pit lap analysis

### Monte Carlo Simulation
- Runs thousands of simulated races
- Models uncertainty in race outcomes
- Uses multiprocessing for faster simulations
- Calculates average, best, worst, and risk metrics

### Risk-Based Decision Engine
Instead of only choosing the fastest strategy, the engine considers consistency and uncertainty:


Score = Average Time + (Risk × Factor)


---

# 📈 Development Progress

## Sprint 1 — Core Simulation
 Built race simulation foundation

- Driver model
- Track model
- Tyre model
- Lap simulation
- Race simulation

## Sprint 2 — Strategy Engine
 Added strategy modelling

- Pit stops
- Tyre switching
- Strategy evaluation

## Sprint 3 — Monte Carlo Simulation
 Added probabilistic race simulation

- Multiple race simulations
- Statistical analysis
- Parallel processing

## Sprint 4 — Risk-Aware Decisions
 Added uncertainty-based strategy selection

- Risk analysis
- Consistency scoring
- Decision engine

## Sprint 5 — Race Environment
 Added foundations for dynamic conditions

- Weather modelling
- Safety car probability
- Environment generation

## Sprint 6 — Strategy Search Improvements
 Added pit window evaluation

The engine now evaluates different pit timings to find stronger strategies.

---

#  Future Improvements

Planned features:

- Weather effects on lap performance
- Dynamic safety car strategy impact
- More realistic race states
- Real F1 data integration using FastF1
- Advanced optimisation algorithms
- Machine learning strategy prediction

---

# 🛠️ Technologies

- Python
- Object-Oriented Programming
- Monte Carlo Simulation
- Multiprocessing
- Statistical Modelling
- Git/GitHub

---

## Current Status

🚧 Active development

Current focus:
Improving race realism and environmental modelling before adding real-world F1 data and AI techniques.
