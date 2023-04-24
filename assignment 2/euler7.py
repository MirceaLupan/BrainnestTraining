# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13. What is the 10001st prime number?

from math import log, isqrt

# To find the nth prime number, the algorithm uses the sieve of Eratosthenes.
# The length of the sieve is 2*n*log(n). The fact that the nth prime number p_n
# satisfies the relation p_n ~ n log(n) is used.
# See https://en.wikipedia.org/wiki/Prime_number_theorem

n = 100001
print(f"n = {n}")
sieve_len = int(2 * n * log(n))
print(f"sieve length = {sieve_len}")

# Sieve of Eratosthenes
sieve = [True] * sieve_len
for i in range(2, isqrt(sieve_len) + 1):
    if sieve[i]:
        for j in range(2 * i, sieve_len, i):
            sieve[j] = False

# count the primes and find the nth prime
count = 0
for i in range(2, sieve_len):
    if sieve[i]:
        count += 1
        if count == n:
            nth_prime = i

# display the results
if count < n:
    print("\nThe length of the sieve is too small!")
else:
    print(f"\ntotal primes = {count}")
    print(f"nth prime = {nth_prime}")
