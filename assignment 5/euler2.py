# We shall say that an n-digit number is pandigital if it makes use of all the digits
# 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital. HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.


def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")


def find_unusual_numbers():
    unusual_numbers = set()
    # if the multiplicand is one digit, then the multiplier must be four digits
    for i in range(1, 10):
        for j in range(1000, 10000):
            # the product cannot contain more than four digits
            if i * j > 9999:
                break
            if is_pandigital(str(i) + str(j) + str(i * j)):
                unusual_numbers.add(i * j)
                print(i, "*", j, "=", i * j)

    # if the multiplicand is two digit, then the multiplier must be three digits
    for i in range(10, 100):
        for j in range(100, 1000):
            # the product cannot contain more than four digits
            if i * j > 9999:
                break
            if is_pandigital(str(i) + str(j) + str(i * j)):
                unusual_numbers.add(i * j)
                print(i, "*", j, "=", i * j)

    return unusual_numbers


unusual_numbers = find_unusual_numbers()
print("Unusual numbers: ", unusual_numbers)
print("Sum: ", sum(unusual_numbers))
