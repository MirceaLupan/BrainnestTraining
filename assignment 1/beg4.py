# Write a program that takes in a list of integers and returns
# the largest number in the list that is also divisible by 3.

from random import randint

# generating a list of random integers
n = 10  # length of the list
numbers = [randint(-50, 50) for i in range(n)]
print(numbers)

# finding the largest number divisible by 3
max = None
for i in range(len(numbers)):
    if numbers[i] % 3 == 0:
        if max is None or max < numbers[i]:
            max, ind = numbers[i], i

# printing the results
if max is None:
    print("The list does not contain integers divisible by 3")
else:
    print(f"The largest number divisible by 3 is {max}, its index is {ind}")
