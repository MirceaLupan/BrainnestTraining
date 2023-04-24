# Then make it output as a dictionary and print the one that sent most emails.

f = open("mbox-short.txt", "r")
senders = []
for line in f:
    words = line.split()
    if len(words) >= 2:
        if words[0] == "From" or words[0] == "From":
            senders.append(words[1])

frequencies = {}
for sender in senders:
    frequencies[sender] = senders.count(sender)

for key, value in frequencies.items():
    print(key, ":  ", value)

print()
max_freq = max(frequencies, key=frequencies.get)
print(max_freq, ": ", frequencies[max_freq])
