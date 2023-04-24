# From mbox-short.txt write a program that gives the output of senders and number of lines.

f = open("mbox-short.txt", "r")
total = 0
for line in f:
    words = line.split()
    if len(words) >= 2:
        if words[0] == "From" or words[0] == "From":
            print("Sender: ", words[1])
            total += 1
print("Total number of lines:", total)
