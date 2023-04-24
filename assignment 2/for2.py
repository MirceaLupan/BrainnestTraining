# Create a for loop that iterates through a list of numbers and prints the square of each number.

from random import randint

# generating a list of n random integers from interval [a,b]
n = 10
a = 0
b = 10
numbers = [randint(a, b) for i in range(n)]

# printing the square of the numbers
for number in numbers:
    print(f"{number} ^ 2 = {number ** 2}")
