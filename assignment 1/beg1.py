# Write a program that prompts the user for a string and
# checks whether the string is a palindrome (i.e., the string
# reads the same forward and backward).

# function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


# main function
print("Check if a string is a palindrome")

s = input("Enter the string: ")
ans = is_palindrome(s)

if ans:
    print("Yes")
else:
    print("No")
