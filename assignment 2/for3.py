# Create a for loop that iterates through a list of dictionaries
# and prints the value of a specified key for each dictionary.

from random import randint

# generating a list of dictionaries of random values and printing it
nd = 10  # number of dictionaries
dicts = [{randint(0, 5): randint(0, 99) for i in range(10)} for j in range(nd)]
print("Generated dictionaries:")
for d in dicts:
    print(d)
print()

# printing the value of specified key for each dictionary
key = 5
print("key: ", key)
for i in range(nd):
    if key in dicts[i]:
        print(f"dictionary #{i}: value = {dicts[i][key]}")
    else:
        print(f"dictionary #{i} does not contain the key")
