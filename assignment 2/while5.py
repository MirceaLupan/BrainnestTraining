# Create a while loop that repeatedly takes user input and
# keeps track of the highest number entered until the user enters "done".

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
    if flag:
        lst.append(x)
    if s == "done":
        break

if not lst:
    print("There are no numbers in the entered data!")
else:
    print("The list of numbers: ", lst)
    print("The highest value: ", max(lst))
