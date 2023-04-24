# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is, 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

# Solution 1
n = 100
s1 = 0
s2 = 0
for i in range(1, n + 1):
    s1 += i ** 2
    s2 += i
diff = s2 ** 2 - s1
print("\nSolution 1")
print(f"The difference is {diff}")

# Solution 2
s1 = n * (n + 1) * (2 * n + 1) // 6
s2 = n * (n + 1) // 2
diff = s2 ** 2 - s1
print("\nSolution 2")
print(f"The difference is {diff}")
