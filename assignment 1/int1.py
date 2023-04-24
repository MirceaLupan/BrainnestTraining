# Write a function that takes a list of integers as an argument,
# and returns the sum of the integers.
# Use a try-except block to catch any ValueError exceptions
# that may be raised when attempting to convert a string to an integer.

def list_sum(lst):
    """return the sum of the integer elements (also integer as string) of a list"""
    sum = 0
    for elem in lst:
        try:
            number = int(elem)
            sum += number
        except ValueError:
            print(f"The element '{elem}' cannot be converted to an integer!")
    return sum


# main function
lst = [1, 5, -1, "2", "-3", "a", 4]
print("List: ", lst)
print("Sum of integers: ", list_sum(lst))
