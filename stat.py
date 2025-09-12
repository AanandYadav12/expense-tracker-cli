import pandas as pd
def total_expenses(data):
    return sum(item["amount"] for item in data)
def average_expenses(data):
    return total_expenses(data) / len(data) if data else 0
def expenses_by_category(data):
    df = pd.DataFrame(data)
    return df.groupby("category")["amount"].sum().to_dict()
