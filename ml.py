import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

def detect_anomalies(data,contamination=0.1):
    df = pd.DataFrame(data)
    X=df[["amount"]]
    model=IsolationForest(contamination=contamination,random_state=42)
    df['anomaly'] = model.fit_predict(X)
    return df
def predict_future_expenses(data,days=30):
    df=pd.DataFrame(data)
    df["date"]=pd.to_datetime(df["date"])
    df["day_num"] = (df["date"] - df["date"].min()).dt.days #finds the earliest date
    # in dataset and calculates days since then.
    X = df[["day_num"]]
    y = df["amount"]
    model = LinearRegression()
    model.fit(X,y)
    future_day = np.array([[df["day_num"].max() + days]])
    prediction = model.predict(future_day)[0]
    return prediction

