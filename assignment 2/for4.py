# Create a for loop that iterates through a list of numbers and prints the largest number in the list.
from random import randint

# generating a list of n random integers
n = 50
numbers = [randint(-100, 100) for i in range(n)]
print(numbers)

# finding the largest number and its index
# assuming that list contains at least one element
max, ind = numbers[0], 0
for i in range(len(numbers)):
    if max < numbers[i]:
        max, ind = numbers[i], i

print(f"The largest value is {max}, its index is {ind}")
