# Write a function that takes a list of dictionaries as an argument,
# and returns the value of a specified key from each dictionary.
# Use a try-except block to catch any KeyError exceptions that may be
# raised when attempting to access a key that does not exist in a dictionary.

from random import randint


def extract_values(key, dicts):
    """extract the values corresponding to specified key from a list of dictionaries"""
    res = []
    for d in dicts:
        try:
            res.append(d[key])
        except KeyError:
            print(f"Dictionary {d} does not contain the key '{key}'!")
    return res


# generating a list of dictionaries of random values and printing it
nd = 10  # number of dictionaries
dicts = [{randint(0, 5): randint(0, 99) for i in range(10)} for j in range(nd)]
print("Generated dictionaries:")
for d in dicts:
    print(d)
print()

# printing the list of values corresponding to specified key
key = 5
print("key: ", key)
print("Resulting list: ", extract_values(key, dicts))
