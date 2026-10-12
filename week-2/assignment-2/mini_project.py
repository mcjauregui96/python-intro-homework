fahrenheit = float(input("Please enter temperature in Fahrenheit: "))
celsius = round((fahrenheit - 32)* 5/9, 1)
print(f'{fahrenheit}\N{DEGREE SIGN}F is {celsius}\N{DEGREE SIGN}C.')