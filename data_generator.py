import json
import random
from datetime import datetime, timedelta

# Categories + sample notes
categories = {
    "food": ["Breakfast", "Lunch", "Dinner", "Snacks", "Coffee"],
    "transport": ["Bus fare", "Taxi", "Metro", "Fuel"],
    "shopping": ["Clothes", "Shoes", "Groceries", "Stationery"],
    "entertainment": ["Movie", "Games", "Concert", "Streaming"],
    "bills": ["Electricity", "Water", "Internet", "Phone recharge"],
    "other": ["Gift", "Donation", "Miscellaneous"]
}

# Generate random expenses for last 60 days
expenses = []
start_date = datetime.today() - timedelta(days=60)
id_counter = 1

for day in range(60):
    date = (start_date + timedelta(days=day)).strftime("%Y-%m-%d")
    for _ in range(random.randint(1, 4)):  # 1–4 expenses per day
        category = random.choice(list(categories.keys()))
        note = random.choice(categories[category])
        amount = random.randint(20, 1000)  # ₹20 to ₹1000
        expenses.append({
            "id": id_counter,
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        })
        id_counter += 1

# Save to expenses.json
with open("expenses.json", "w") as f:
    json.dump(expenses, f, indent=2)

print(f" Generated {len(expenses)} dummy expenses in expenses.json")
