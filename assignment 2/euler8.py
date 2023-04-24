# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet(n):
    """find the first Pythagorean triplet a,b,c, where a+b+c=n, if exists"""
    print(f"\nn = {n}")
    # Only values for which a <= b <= c are checked
    for a in range(1, n // 3 + 1):
        for b in range(a, (n - a) // 2 + 1):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(f"a = {a}, b = {b}, c = {c}")
                print(f"abc = {a * b * c}")
                return
    print(f"There is no pythagorean triplet such that a + b + c = {n}!")


n = 1000
pythagorean_triplet(n)

n = 100
pythagorean_triplet(n)
