"""
Mini Project: Weather-Based Walk Predictor using Decision Tree Classifier
AI Lab Coursework - Supervised Machine Learning & Decision Trees

Description:
    Predicts whether a person should go outside for a walk (1 = Go Outside)
    or stay indoors (0 = Stay Inside) based on weather conditions:
    Temperature (°C) and Chance of Rain (%).
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text


def create_simulated_dataset() -> pd.DataFrame:
    """
    Creates a simulated dataset representing past days with weather metrics:
    - Temperature (in Celsius)
    - Chance of Rain (in percentage, 0 to 100%)
    - Go Outside: 1 (Yes, go for a walk), 0 (No, stay inside)
    """
    data = {
        "Temperature": [
            10, 12, 14, 18, 20, 22, 24, 25, 27, 28,
            30, 32, 35, 38, 5, 8, 16, 21, 23, 26,
            19, 22, 29, 33, 15, 11, 24, 27, 31, 17
        ],
        "Chance of Rain": [
            80, 60, 45, 10, 15, 5, 10, 20, 25, 30,
            15, 65, 85, 90, 20, 70, 75, 10, 50, 80,
            5, 30, 70, 40, 10, 85, 25, 15, 85, 35
        ],
        "Go Outside": [
            0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            1, 1, 0, 0, 1, 0, 1, 1, 0, 1
        ],
    }
    return pd.DataFrame(data)


def train_walk_predictor(df: pd.DataFrame):
    """
    Trains a Decision Tree Classifier on the weather dataset.
    Features: ['Temperature', 'Chance of Rain']
    Target: 'Go Outside'
    """
    feature_cols = ["Temperature", "Chance of Rain"]
    X = df[feature_cols]
    y = df["Go Outside"]

    # Initialize DecisionTreeClassifier
    clf = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
    clf.fit(X, y)

    return clf, feature_cols


def predict_walk_decision(clf: DecisionTreeClassifier, feature_names: list, temp: float, rain_chance: float):
    """Predicts walk decision for given temperature and chance of rain."""
    sample = pd.DataFrame([[temp, rain_chance]], columns=feature_names)
    prediction = clf.predict(sample)[0]
    probabilities = clf.predict_proba(sample)[0]

    label = "Go Outside for a Walk" if prediction == 1 else "Stay Inside"
    confidence = probabilities[prediction] * 100

    return prediction, label, confidence


def main():
    print("=" * 65)
    print("Mini Project: Weather-Based Walk Predictor (Decision Tree)")
    print("=" * 65)

    # 1. Create and display simulated dataset
    df = create_simulated_dataset()
    print("\n[1] Simulated Historical Weather Dataset (First 10 records):")
    print(df.head(10).to_string(index=False))
    print(f"\nTotal Records: {len(df)} days | Features: Temperature (°C), Chance of Rain (%)")

    # 2. Train Decision Tree Classifier
    clf, feature_names = train_walk_predictor(df)
    train_acc = clf.score(df[feature_names], df["Go Outside"]) * 100
    print(f"\n[2] Model Training Completed.")
    print(f"    Classifier: DecisionTreeClassifier (max_depth=4)")
    print(f"    Training Set Accuracy: {train_acc:.1f}%")

    # 3. Display Tree Rules
    print("\n[3] Learned Decision Rules:")
    tree_rules = export_text(clf, feature_names=feature_names)
    print(tree_rules)

    # 4. Sample Predictions
    print("[4] Sample Walk Predictions:")
    test_cases = [
        (22, 10, "Mild temperature and very low chance of rain"),
        (35, 80, "Hot temperature with high chance of rain"),
        (8, 15, "Very cold weather despite low rain"),
        (26, 25, "Warm temperature with moderate rain probability"),
        (18, 75, "Comfortable temperature but heavy rain likelihood"),
    ]

    for temp, rain, scenario in test_cases:
        pred_code, decision_label, conf = predict_walk_decision(clf, feature_names, temp, rain)
        status_tag = "[YES - GO OUTSIDE]" if pred_code == 1 else "[NO  - STAY INSIDE]"
        print(f"\n  Scenario     : {scenario}")
        print(f"  Conditions   : Temperature = {temp}°C, Chance of Rain = {rain}%")
        print(f"  Result       : {status_tag} -> {decision_label} (Confidence: {conf:.1f}%)")


if __name__ == "__main__":
    main()

