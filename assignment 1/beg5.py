# Write a program that prompts the user for a number and checks
# whether the number is a prime number (i.e., only divisible by 1 and itself).

from math import isqrt


def is_prime(n):
    """check if an integer is a prime number"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input("Enter an integer: "))
print(f"{n} is prime? {is_prime(n)}")
