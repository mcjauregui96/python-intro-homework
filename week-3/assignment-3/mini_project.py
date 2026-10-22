# Ask the user for a day of the week and a time of day
day_of_week = input("Please enter a day of the week: ").strip().lower()
time_of_day = input("Please enter a time of day: ").strip().lower()
# validate the day of the week and time of day inputs
if day_of_week not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Invalid day of the week entered. Please enter a valid day (Monday, Tuesday, etc.).")
elif time_of_day not in ["morning", "afternoon", "evening"]:
    print("Invalid time of day entered. Please enter a valid time (morning, afternoon, or evening).")    
elif day_of_week != "monday" and day_of_week != "friday" and day_of_week != "sunday":
    print(f"It's {day_of_week.capitalize()}! There's nothing planned for today.")
elif day_of_week == "monday":
    if time_of_day == "morning":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Time to get ready for school.")
    elif time_of_day == "afternoon":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Time to finish up your work.")
    else:
        print("You're done for today, enjoy your evening!")

elif day_of_week == "friday":
    if time_of_day == "morning":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Remember to call grandma.")
    elif time_of_day == "afternoon":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Meet mom for lunch at Vinny's.")
    else:
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Go to the club!!!")

else:
    if time_of_day == "morning":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Time to go to church.")
    elif time_of_day == "afternoon":
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Time to relax and watch some TV.")
    else:
        print(f"It's {day_of_week.capitalize()} {time_of_day}! Time to wind down and prepare for the week ahead.")

