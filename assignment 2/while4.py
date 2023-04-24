# Create a while loop that repeatedly takes user input and appends it to a list,
# but only if the input is a number greater than 10.

def is_number(s):
    """check if a string is a float"""
    try:
        x = 0
        x = float(s)
    except:
        flag = False
    else:
        flag = True
    return [x, flag]


# main function
lst = []
while True:
    s = input("Enter a string: ")
    x, flag = is_number(s)
    if flag and x > 10:
        lst.append(x)
    if s == "done":
        break

print("The list of numbers greater then 10: ", lst)
