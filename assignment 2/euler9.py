# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import log, isqrt

n = 2_000_000
print(f"\nn = {n}")

# Sieve of Eratosthenes
sieve = [True] * n
for i in range(2, isqrt(n) + 1):
    if sieve[i]:
        for j in range(2 * i, n, i):
            sieve[j] = False

# count the primes and calculate the sum
count = 0
sum = 0
for i in range(2, n):
    if sieve[i]:
        count += 1
        sum += i

# display the results
print(f"Total primes = {count}")
print(f"Sum of the primes = {sum}")
