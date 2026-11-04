#Copy the students list from that file into your script.

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

#Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
top_score = students[0]["score"]
top_scorer = students[0]["name"]
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_scorer = student["name"]
print(f'Top scorer: {top_scorer} ({top_score})')

#Calculate the class average — accumulate the total score in a loop, then divide.
total = 0 
for student in students:
    total += student["score"]
average = total / len(students)
print(f'Class average: {average:.2f}')

#List all unique subjects — use a set to collect subjects as you loop, then print them.
subjects = set()
for student in students:
    subjects.add(student["subject"])
print(f'Subjects offered: {subjects}')

#List high scorers — use a loop and .append() to get the names of all students who scored above 75.
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f'High scorers: {high_scorers}')