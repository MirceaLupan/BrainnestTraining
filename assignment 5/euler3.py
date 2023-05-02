# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from math import gcd

numerator = 1
denominator = 1
for i in range(1, 10):
    for j in range(i + 1, 10):
        for d in range(1, 10):
            # check case i/j=id/jd (no matches)
            if i * (10 * j + d) == j * (10 * i + d):
                numerator *= i
                denominator *= j
                print(i, "/", j, "  =  ", 10 * i + d, "/", 10 * j + d)
            # check case i/j=id/dj (4 matches)
            if i * (10 * d + j) == j * (10 * i + d):
                numerator *= i
                denominator *= j
                print(i, "/", j, "  =  ", 10 * i + d, "/", 10 * d + j)
            # check case i/j=di/jd (no matches)
            if i * (10 * j + d) == j * (10 * d + i):
                numerator *= i
                denominator *= j
                print(i, "/", j, "  =  ", 10 * d + i, "/", 10 * j + d)
            # check case i/j=di/dj (no matches)
            if i * (10 * d + j) == j * (10 * d + i):
                numerator *= i
                denominator *= j
                print(i, "/", j, "  =  ", 10 * d + i, "/", 10 * d + j)

print("Denominator:", denominator // gcd(numerator, denominator))
