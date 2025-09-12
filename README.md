# expense-tracker-cli
## 🚀 Features

### 📊 Statistics Module
- **Total Expenses** → Sum of all expenses.  
- **Average Expenses** → Daily average spending.  
- **Expenses by Category** → Breakdown of spending across categories.  

### 🤖 Machine Learning Module
- **Monthly Expense Prediction** → Uses **Linear Regression** to predict monthly expenses.  
- **Anomaly Detection** → Uses **Isolation Forest** to detect unusual spending patterns.  

### 🛠️ Data Generator
- Creates **dummy expense data** in JSON format for testing.  

--

### 📌 What is `main.py`?

`***main.py` is the **entry point** of the Expense Tracker CLI.  
It connects all the modules (`stat.py`, `ml.py`, `data_generator.py`) and allows you to interact with the project from the command line.  

### Responsibilities of `main.py`:
1. **Expense Management**  
   - Loads existing expenses from `expenses.json`.  
   - Saves new expenses back into the file.  

2. **Statistics**  
   - Computes **total expenses**.  
   - Calculates **daily average expenses**.  
   - Breaks down **expenses by category**.  
   - Finds the **top spending category**.  

3. **Machine Learning**  
   - Prepares data for ML models.  
   - Works with `ml.py` to:  
     - Predict **monthly expenses** using **Linear Regression**.  
     - Detect **anomalies** in spending using **Isolation Forest**.  

4. **Controller Role**  
   - Acts as the **main driver** of the project.  
   - Connects statistics, machine learning, and data generation into a single CLI tool.  

👉 Simply put: `main.py` is where you run the project and tie everything together***.  

---




