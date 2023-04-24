# Create a while loop that repeatedly takes user input and
# appends it to a list, but only if the input is a unique string.

lst = []
while True:
    s = input("Enter a string: ")
    if s in lst:
        print("> The string is not unique!")
    else:
        print("> The string is unique!")
        lst.append(s)
    if s == "done":
        break

print(lst)
