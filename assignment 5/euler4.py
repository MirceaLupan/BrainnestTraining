# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math

factorials = [math.factorial(x) for x in range(10)]


def factorial_sum(n):
    return sum([factorials[int(x)] for x in str(n)])


sm = 0  # sum of the curious numbers

# The sum of the factorials of the digits is maximum if the number consists
# only of the digit 9. For numbers consisting of more than 8 digits, this sum
# is smaller than the given number. So only for numbers consisting of at most
# 7 digits, the sum of the factorials could be equal to the given number.
for n in range(10, 1000000):
    if n == factorial_sum(n):
        sm += n
        print(n, factorial_sum(n))

print("\nSum: ", sm)
