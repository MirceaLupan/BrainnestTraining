# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def sum_digits(n):
    return sum([int(x) for x in list(str(n))])


print(sum_digits(2 ** 15))
print(sum_digits(2 ** 100))
