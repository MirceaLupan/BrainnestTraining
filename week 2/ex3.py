# Try converting the content of a txt file in upper case (on the console).

try:
    f = open("demofile.txt", "r")
    for s in f:
        print(s.upper(), end="")
    f.close()
except:
    print("An error occurs")
