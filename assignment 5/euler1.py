# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import collections


def count_ways(amount, coins):
    """Count the ways in which the amount of money can be decomposed."""

    def rec(first):
        """Recursive function used to obtain decompositions"""
        for i in range(first, len(coins)):
            nonlocal sum
            sum += coins[i]
            way.append(coins[i])
            if sum < amount:
                rec(i)
            elif sum == amount:
                nonlocal count
                count += 1
                # print(way)
            sum -= coins[i]
            way.pop()

    count = 0
    sum = 0
    way = []
    rec(0)
    return count


coins = [200, 100, 50, 20, 10, 5, 2, 1]
print("Coins:", coins)

amount = 200
print("\nAmount:", amount)
print("Number of ways:", count_ways(amount, coins))

amount = 55
print("\nAmount:", amount)
print("Number of ways:", count_ways(amount, coins))
