# Create a while loop that repeatedly takes user input and adds the input to a list until the user enters "done".

lst = []
while True:
    s = input("Enter a string: ")
    lst.append(s)
    if s == "done":
        break

print(lst)
