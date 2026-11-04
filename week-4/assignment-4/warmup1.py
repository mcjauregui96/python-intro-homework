#create a list of numbers. Without using any loops.
number = [50, 60, 70, 80, 90, 100, 110, 120]
# The first item
print("First:", number[0])
# The last item (use a negative index)
print("Last:", number[-1])
# A slice containing only the middle four items
print("Middle:",number[2:6])
# The full list in reverse order
number.reverse()
print("Reversed:",number)
