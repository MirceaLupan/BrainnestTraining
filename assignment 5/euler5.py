# The number, 197, is called a circular prime because all rotations
# of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from math import isqrt


def rotation(n):
    """generating all rotations of a given number"""
    n = str(n)
    n0 = n
    while True:
        n = n[1:] + n[0]
        if n == n0:
            return
        yield int(n)


n = 1_000_000
print(f"n = {n}")

# finding all prime numbers under 1000000
sieve = [True] * n
for i in range(2, isqrt(n) + 1):
    if sieve[i]:
        for j in range(2 * i, n, i):
            sieve[j] = False

# finding all circular primes
for i in range(11, n):
    if sieve[i]:
        for j in rotation(i):
            if not sieve[j]:
                sieve[i] = False
                break

# printing the result
print("Circular primes less than n:")
count = 0
for i in range(2, n):
    if sieve[i]:
        count += 1
        print(i)
print(f"Total numbers: {count}")
