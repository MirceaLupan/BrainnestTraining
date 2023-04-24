# Write a program that prompts the user for their age
# and checks whether they are old enough to vote (i.e., 18 years old or older).

print("Hello user!")
age = int(input("Please, tell me how old you are: "))
if age < 18:
    print("\nYou are too young to vote!")
else:
    print("\nYour age gives you the right to vote!")
