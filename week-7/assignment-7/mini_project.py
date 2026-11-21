# expense_report.py
import csv
import os
from datetime import datetime


def generate_report(category):
    """Generate a report for the given category and write it to <category>_report.txt."""

    # 1. Verify the input file exists
    input_path = os.path.join("..", "data", "expenses.csv")
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    # 2. Read the CSV into a list of dictionaries
    with open(input_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # 3. Convert the amount field to float for each row
    for row in rows:
        row["amount"] = float(row["amount"])

    # 4. Filter to only rows matching the category
    filtered = [row for row in rows if row["category"] == category]

    # 5. Calculate the total
    total = sum(row["amount"] for row in filtered)

    # 6. Write the report
    output_path = f"{category.lower()}_report.txt"
    today = datetime.now().strftime("%B %d, %Y")

    with open(output_path, "w") as out:
        out.write(f"{category} Expense Report — generated {today}\n")
        for row in filtered:
            out.write(f"{row['date']}: ${row['amount']:.2f}\n")
        out.write(f"Total: ${total:.2f}\n")

    print(f"Report written to {output_path}")


if __name__ == "__main__":
    generate_report("Food")