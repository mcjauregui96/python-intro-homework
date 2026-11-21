#Use csv.DictReader to read ../data/students.csv — it has three columns: name, subject, and score. Print each student's name and score on a single line.
import csv

with open("../data/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")