# Create a while loop that generates random numbers and adds them
# to a list until the sum of all numbers in the list is greater than 100.

from random import randint

lst = []
sum = 0
while sum <= 100:
    lst.append(randint(0, 9))
    sum += lst[-1]

print(f"List of randoms: {lst}")
print(f"Their sum: {sum}")
