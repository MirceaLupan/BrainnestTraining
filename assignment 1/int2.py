# Write a function that takes a filename as an argument, and attempts to open the file.
# Use a try-except block to catch any FileNotFoundError exceptions that may be raised
# when attempting to open the file. If the file is successfully opened, the function
# should return the contents of the file.


def file_contents(file_name):
    """returns the contents of a file if it exists"""
    contents = ""
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        print(f"File '{file_name}' not found!")
    else:
        contents = f.read()
        f.close()
    return contents


print(file_contents("file.txt"))
print(file_contents("demofile.txt"))
