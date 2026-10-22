num = int(input("Enter a number: "))

# --- Sign block ---
if num > 0:
    print(f'{num} is positive.')
elif num < 0:
    print(f'{num} is negative.')
else:
    print(f'{num} is zero.')

# --- Parity block ---
if num % 2 == 0:
    print(f'{num} is even.')
else:
    print(f'{num} is odd.')