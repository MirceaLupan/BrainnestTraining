# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ten_1 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen"]

count = 0
for m in range(1, 1001):
    ss = str(m)
    ss = "0" * (4 - len(ss)) + ss
    digits = [int(x) for x in ss]

    s = ""
    if digits[0] != 0:
        s = units[digits[0] - 1] + " thousand"
        if digits[1] + digits[2] + digits[3] != 0:
            s = s + " "

    if digits[1] != 0:
        s = s + units[digits[1] - 1] + " hundred"
        if digits[2] + digits[3] != 0:
            s = s + " and "

    if digits[2] != 0:
        if digits[3] == 0:
            s = s + tens[digits[2] - 1]
        elif digits[2] == 1:
            s = s + ten_1[digits[3] - 1]
        else:
            s = s + tens[digits[2] - 1] + " " + units[digits[3] - 1]

    if digits[2] == 0 and digits[3] != 0:
        s = s + units[digits[3] - 1]
    print(m, " - ", s)
    count += len(s.replace(" ", ""))

print("\nNumber of letters:", count)
