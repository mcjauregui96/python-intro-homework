#Build a menu-driven program using a while loop. Each time the menu displays, the user picks an option. 

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    
    choice = input("Please select an option (1-5): ")
    if choice == '1':
        smallest = numbers[0]
        for index in range(1, len(numbers)):
            if numbers[index] < smallest:
                smallest = numbers[index]
        print(f"The minimum number is: {smallest}")
    elif choice == '2':
        largest = numbers[0]
        for index in range(1, len(numbers)):
            if numbers[index] > largest:
                largest = numbers[index]
        print(f"The maximum number is: {largest}")
    elif choice == '3':
        target = int(input("Enter a number to search for: "))
        found = False
        for index in range(len(numbers)):
            if numbers[index] == target:
                print(f"Number {target} found at index {index}")
                found = True
                break
        if not found:
            print(f"Number {target} not found in the list.")
    elif choice == '4':
        def bubble_sort(numbers):
            copy = numbers[:]
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(copy) - 1):
                    if copy[i] > copy[i + 1]:
                        copy[i], copy[i + 1] = copy[i + 1], copy[i]
                        swapped = True
            return copy 
    
        print("The list has been sorted.")
        print(f"Sorted list: {bubble_sort(numbers)}")
    elif choice == '5':
        print("You're exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")