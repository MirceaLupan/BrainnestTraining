# Write a function that takes a list of integers as an argument,
# and returns the largest integer in the list. Use a try-except block
# to catch any ValueError exceptions that may be raised when attempting
# to compare elements that are not integers.

from random import randint


def largest(lst):
    """returns the largest element of a list and its index"""
    max, ind = None, None
    for i in range(len(numbers)):
        try:
            if max is None or max < int(numbers[i]):
                max, ind = int(numbers[i]), i
        except ValueError:
            print(f"Element '{numbers[i]}' is not an integer")
    if max is None:
        print("The list is empty or does not contain integers")
    else:
        print(f"The largest value is {max}, its index is {ind}")
    return max, ind


# testing list #1
n = 20
numbers = [randint(-100, 100) for i in range(n)]
print("\nList: ", numbers)
largest(numbers)

# testing list #2
numbers = [5, '55', 7, 'x', 0, 2]
print("\nList: ", numbers)
largest(numbers)

# testing list #3
numbers = ['abc', 'x']
print("\nList: ", numbers)
largest(numbers)
