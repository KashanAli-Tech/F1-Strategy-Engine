# 🏎️ F1 Strategy Engine 

A probabilistic Formula 1 race strategy optimisation engine that uses Monte Carlo simulation, uncertainty modelling, and optimisation algorithms to evaluate thousands of race scenarios and identify optimal strategies.
The system models tyre degradation, driver performance, pit strategies, weather conditions, safety car events, and race uncertainty to simulate possible outcomes and make risk-aware strategy decisions rather than relying on a single deterministic prediction.
Built using Python, the project explores simulation engineering, quantitative modelling, and decision systems with the long-term goal of integrating real F1 data and machine learning techniques.

---

## Features

### Race Simulation
- Lap-by-lap race simulation
- Driver performance modelling
- Fuel effects
- Tyre degradation and tyre cliff behaviour
- Pit stop simulation
- Safety car event modelling
- Dynamic weather transitions

### Tyre & Strategy Modelling
- Soft, Medium, and Hard tyre compounds
- Different tyre degradation behaviours
- One-stop and two-stop strategy generation
- Strategy validation
- Variable pit window analysis
- Strategy evaluation and comparison

### Monte Carlo Simulation
- Runs thousands of simulated races
- Models uncertainty in race outcomes
- Uses multiprocessing for faster simulations
- Calculates average, best, worst, and risk metrics
- Evaluates strategy consistency across scenarios

### Risk-Based Decision Engine
Instead of only choosing the fastest strategy, the engine considers consistency and uncertainty:


Score = Average Time + (Risk × Factor)


---

# 📈 Development Progress

## Sprint 1: Core Simulation
 Built race simulation foundation

- Driver model
- Track model
- Tyre model
- Lap simulation
- Race simulation

## Sprint 2: Strategy Engine
 Added strategy modelling

- Pit stops
- Tyre switching
- Strategy evaluation
- Strategy generation

## Sprint 3: Monte Carlo Simulation
 Added probabilistic race simulation

- Multiple race simulations
- Statistical analysis
- Parallel processing

## Sprint 4: Risk-Aware Decisions
 Added uncertainty-based strategy selection

- Risk analysis
- Consistency scoring
- Decision engine

## Sprint 5: Race Environment
 Added foundations for dynamic conditions

- Weather modelling with transition probabilities
- Safety car modelling
- Environment generation
- Race condition simulation

## Sprint 6: Strategy Search Improvements
 Added advanced strategy evaluation

The engine now evaluates different pit timings and multi-stop strategies to find stronger race strategies.

---

#  Future Improvements

Planned features:

- Configuration system for simulation parameters
- Real F1 data integration using FastF1
- Historical race parameter calibration
- Strategy backtesting against real races
- Advanced optimisation algorithms
- Machine learning strategy prediction

---

# 🛠️ Technologies

- Python
- Object-Oriented Programming
- Monte Carlo Simulation
- Multiprocessing
- Statistical Modelling
- Probability Models
- Git/GitHub

---

## Current Status

🚧 Active development

Current focus:
Improving simulator architecture, calibrating race models, and preparing integration with real-world F1 data and AI techniques.
