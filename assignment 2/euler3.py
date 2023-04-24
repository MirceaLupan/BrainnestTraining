# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600_851_475_143
print("n: ", n)
prime_factors = []

i = 2
while n != 1:
    if n % i == 0:
        prime_factors.append(i)
        n //= i
    else:
        i += 1

print("prime factors: ", prime_factors)
print("largest prime factor:", prime_factors[-1])
