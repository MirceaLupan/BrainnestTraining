# Create a for loop that iterates through a list of lists
# and prints the sum of the elements in each sub-list.

from random import randint

# generating a list of sub-lists of random values and printing it
n = 10  # number of sub-lists
lists = [[randint(-50, 50) for i in range(10)] for j in range(n)]
print("Generated lists:")
for lst in lists:
    print(lst)
print()

# printing the sum of each sub-list
for i in range(len(lists)):
    print(f"Sub-list #{i}, sum: {sum(lists[i])}")
