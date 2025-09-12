import json
import os
from collections import defaultdict
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
from datetime import datetime


expense_file = str(os.path.join(os.path.dirname(__file__), "expenses.json"))

def load_expenses():
    if os.path.exists(expense_file):
        with open(expense_file, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(expense_file, "w") as f:
        json.dump(expenses, f, indent=2)

# -----------------------------
# Statistics Module
# -----------------------------
def total_expenses(expenses):
    return sum(e["amount"] for e in expenses)

def expenses_by_category(expenses):
    cat = defaultdict(int)
    for e in expenses:
        cat[e["category"]] += e["amount"]
    return dict(cat)

def daily_average(expenses):
    days = {e["date"] for e in expenses}
    return round(total_expenses(expenses) / len(days), 2) if days else 0

def top_category(expenses):
    cats = expenses_by_category(expenses)
    return max(cats, key=cats.get) if cats else None

# -----------------------------
# Machine Learning Module
# -----------------------------
def prepare_ml_data(expenses):
    """Convert expenses into (X, y) for regression (date → amount)."""
    dates = []
    amounts = []
    for e in expenses:
        day = datetime.strptime(e["date"], "%Y-%m-%d").toordinal()
        dates.append([day])
        amounts.append(e["amount"])
    return np.array(dates), np.array(amounts)

def predict_future(expenses, future_date: str):
    """Predict expense for a given date using Linear Regression."""
    if len(expenses) < 2:
        return None  # not enough data

    X, y = prepare_ml_data(expenses)
    model = LinearRegression()
    model.fit(X, y)

    future_day = datetime.strptime(future_date, "%Y-%m-%d").toordinal()
    pred = model.predict([[future_day]])
    return round(pred[0], 2)

def detect_anomalies(expenses, contamination=0.2):
    """Detect anomalies in expenses using IsolationForest."""
    if not expenses:
        return pd.DataFrame()

    df = pd.DataFrame(expenses)
    model = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly"] = model.fit_predict(df[["amount"]])
    return df

# -----------------------------
# Unified CLI
# -----------------------------
if __name__ == "__main__":
    expenses = load_expenses()

    print("📊 Expense Stats")
    print("Total:", total_expenses(expenses))
    print("By Category:", expenses_by_category(expenses))
    print("Daily Average:", daily_average(expenses))
    print("Top Category:", top_category(expenses))

    print("\n🤖 ML Prediction")
    future = "2025-09-15"
    prediction = predict_future(expenses, future)
    if prediction:
        print(f"Predicted spending on {future}: {prediction}")
    else:
        print("Not enough data to predict.")

    print("\n🚨 Anomaly Detection")
    anomalies = detect_anomalies(expenses)
    if not anomalies.empty:
        print(anomalies[["date", "amount", "category", "anomaly"]])
    else:
        print("No data for anomaly detection.")

