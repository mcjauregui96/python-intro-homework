age = int(input("Please enter your age: "))
if age >= 0 and age <= 12:
    print(f'Enter your age: {age} \nYou are a Child.')
elif age >= 13 and age <= 17:
    print(f'Enter your age: {age} \nYou are a Teen.')
elif age >= 18 and age <= 64:
    print(f'Enter your age: {age} \nYou are an Adult.')
else:
    print(f'Enter your age: {age} \nYou are a Senior.')