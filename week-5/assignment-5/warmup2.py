#Use a while loop that repeatedly asks the user to enter a positive integer. 
#If the user enters anything that isn't a positive integer, print a message and ask again. 
# Once valid input is received, print it and stop. 

while True:
    try:
        user_input = int(input("Please enter a positive integer: "))
        if user_input > 0:
            print(f"Got it: {user_input}")
            break
        else:
            print("That's not a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")