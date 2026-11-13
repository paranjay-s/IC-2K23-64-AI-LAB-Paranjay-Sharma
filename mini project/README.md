# Mini Project: Weather-Based Walk Predictor

**Student:** Paranjay Sharma (IC-2K23-64)  
**Course:** MCA 7th Semester - Artificial Intelligence Laboratory  

---

## Overview

This mini-project implements a **Decision Tree Classifier** using Python and `scikit-learn` to decide whether a person should go outside for a walk or stay indoors based on simulated weather metrics.

### Features & Target

- **Features**:
  1. `Temperature`: Ambient temperature in degrees Celsius (°C).
  2. `Chance of Rain`: Likelihood of rain as a percentage (0% to 100%).
- **Target Label**:
  - `1`: **Go Outside** (Weather is pleasant with low chance of rain).
  - `0`: **Stay Inside** (Weather is unfavorable—extreme heat, freezing cold, or high probability of rain).

---

## Algorithm Details

- **Model**: `sklearn.tree.DecisionTreeClassifier`
- **Criterion**: Gini Impurity
- **Dataset**: Synthesized historical weather observation table generated using `pandas` and `numpy`.
- **Interpretability**: The decision boundaries split on temperature ranges and rain thresholds, demonstrating transparent machine learning decision logic.

---

## How to Run

Ensure the dependencies (`scikit-learn`, `pandas`, `numpy`) are installed, then execute from the repository root:

```bash
python3 "mini project/weather_walk_predictor.py"
```

### Example Prediction Output

- **Conditions**: Temperature = `22°C`, Chance of Rain = `10%`
- **Model Output**: `1 (Go Outside for a Walk)` with 100% confidence.
