# Create a for loop that iterates through a list of numbers and prints the largest number in the list.

numbers = [5, -3, 12, 8, 17, 0, -7]
print(numbers)
max = numbers[0]
for n in numbers:
    if max < n:
        max = n
print("max =", max)
