# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# that is evenly divisible by all the numbers from 1 to 20?

# Solution 1
from math import lcm

n = 20
res = lcm(*range(1, n + 1))
print("\nSolution 1")
print(f"The Least Common Multiple of the numbers from 1 to {n} is {res}.")


# Solution 2
def gcd(a, b):
    """return the great common divisor of two numbers"""
    while b != 0:
        [a, b] = [b, a % b]
    return a


def lcm(a, b):
    """return the least common multiple of two numbers"""
    return a // gcd(a, b) * b


res = 1
for i in range(1, 20):
    res = lcm(res, i)

print("\nSolution 2")
print(f"The Least Common Multiple of the numbers from 1 to {n} is {res}.")
