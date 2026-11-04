#Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:
list1 = ["Python", "JavaScript", "C++", "Java", "Ruby"]
list2 = ["Python", "Java", "C#", "Go", "Rust"]
set1 = set(list1)
set2 = set(list2)
#The union (all languages from both lists, no duplicates)
print(set1.union(set2))
#The intersection (languages in both lists)
print(set1.intersection(set2))
#The difference (languages only in the first list)
print(set1.difference(set2))