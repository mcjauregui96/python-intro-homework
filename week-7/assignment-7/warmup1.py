#Open ../data/notes.txt using a with block, read it line by line, and print each line with its number.

with open("../data/notes.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    print(f"Line {i + 1}: {lines[i].strip()}") 