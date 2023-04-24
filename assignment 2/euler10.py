# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

from math import isqrt


def divisors(n):
    """return the number of divisors of number n"""
    count = 0
    for i in range(1, isqrt(n)):
        if i * (n // i) == n:
            count += 2
    if isqrt(n) ** 2 == n:
        count += 1
    return count


min_num_divs = 500  # the minimum number of divisors
n = 1  # the order of the triangle number
tn = 1  # the triangle number of order n
while True:
    n_div = divisors(tn)
    if n_div > min_num_divs:
        print(f"n = {n}")
        print(f"The nth triangle number = {tn}")
        print(f"The number of divisors = {n_div}")
        break;
    n += 1
    tn += n