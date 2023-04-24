# Write a function that takes a list of strings as an argument, and returns
# a new list containing only the strings that can be successfully converted
# to a float. Use a try-except block to catch any ValueError exceptions that
# may be raised when attempting to convert a string to a float.


def float_strings(lst):
    """returns a list of the elements that can be converted to float"""
    res = []
    for elem in lst:
        try:
            float(elem)
            res.append(elem)
        except ValueError:
            print(f"The element '{elem}' cannot be converted to a float!")
    return res


# main function
lst = [0, 5.2, '-1.4', -1, "2x", "a", 4.5]
print("List: ", lst)
print()
print("Resulting list: ", float_strings(lst))
