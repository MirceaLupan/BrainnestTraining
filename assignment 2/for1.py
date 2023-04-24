# Create a for loop that iterates through a list of strings and prints each string in uppercase.
import string

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print(text)
words = [word.strip(string.punctuation) for word in text.split()]
print(words)

# Solution 1
print("\nSolution 1")
for word in words:
    print(word.upper())

# Solution 2
print("\nSolution 2")
up_words = [word.upper() for word in words]
for word in up_words:
    print(word)
