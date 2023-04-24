# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max_palindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        n = i * j
        digits = list(str(n))
        if digits == digits[::-1] and max_palindrome < n:
            max_palindrome = n
            [n1, n2] = [i, j]

print(f"The largest palindrome is {max_palindrome} = {n1} * {n2}")
