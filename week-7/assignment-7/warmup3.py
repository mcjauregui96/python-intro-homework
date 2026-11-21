import os

# 1. Print the current working directory
print("Current working directory:", os.getcwd())

# 2. Check whether ../data/expenses.csv exists
path = "../data/expenses.csv"
if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the path with os.path.join() from its parts
joined_path = os.path.join("..", "data", "expenses.csv")
print("Joined path:", joined_path)