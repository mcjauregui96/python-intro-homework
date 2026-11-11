#Start with a hardcoded list of names. Ask the user to enter a name. 
#Loop through the list and print whether the name was found and at what index — 
#or a not-found message if it isn't in the list. 
def linear_search(names, target):
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            return i
    return -1


names = ["Mario", "Luigi", "Peach", "Toad", "Yoshi"]
user_input = input("Please enter a character name from Super Mario: ").strip() 
index = linear_search(names, user_input)
if index != -1:
    print(f"Found {user_input} at index {index}.")
else:
    print(f"{user_input} was not found in the list.")