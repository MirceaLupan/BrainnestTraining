# A perfect number is a number for which the sum of its proper divisors is exactly
# equal to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
# that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum
# of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from math import isqrt


def is_abundant(n):
    sum = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum > n


max = 28124
abundant = [False] * max
for i in range(1, max):
    abundant[i] = is_abundant(i)

abundant_sum = [False] * max
for i in range(1, max):
    for j in range(1, i // 2 + 1):
        if abundant[j] and abundant[i - j]:
            abundant_sum[i] = True
            break

print("The sum of all numbers which cannot be written as the sum of the two abundant numbers:",
      sum([x for x in range(1, max) if not abundant_sum[x]]))

print("The greatest number which cannot be written as the sum of two abundant numbers: ", end="")
for i in range(max - 1, 0, -1):
    if not abundant_sum[i]:
        print(i)
        break
