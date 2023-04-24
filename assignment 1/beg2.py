# Write a program that takes in a list of integers
# and returns the sum of all even numbers in the list.

def sum_of_even_numbers(list):
    """return the sum of even numbers of a list"""
    even_numbers = [x for x in list if x % 2 == 0]
    return sum(even_numbers)


# main function
print("Sum of even numbers of a list of integers\n")

# test function for two given lists
lst = [1, 2, 3, 4, 5, 6, 7]
res = sum_of_even_numbers(lst)
print("list 1: ", lst)
print("sum: ", res)

lst = [-4, 7, 1, 0, 12, -3, -2]
res = sum_of_even_numbers(lst)
print("list 2: ", lst)
print("sum: ", res)

# calculate the sum of the user list
user_string = input("\nEnter a list of integers separated by space: ")
user_list = user_string.strip().split()
user_ints = [int(s) for s in user_list]
print("user list:", user_ints)
res = sum_of_even_numbers(user_ints)
print("sum: ", res)
