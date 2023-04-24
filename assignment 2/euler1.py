# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Solution 1
# check each number if it is multiple and then calculate the sum
max = 1000
sum = 0
for n in range(1, max):
    if n % 3 == 0 or n % 5 == 0:
        sum += n
print("\nSolution 1")
print("sum: ", sum)

# Solution 2
# calculate the sum of the multiples, using the formula
# 1+2+3+...+n=n(n+1)/2
max = 999
sum1 = 3 * ((max // 3) * (max // 3 + 1) // 2)
sum2 = 5 * ((max // 5) * (max // 5 + 1) // 2)
sum3 = 15 * ((max // 15) * (max // 15 + 1) // 2)
sum = sum1 + sum2 - sum3
print("\nSolution 2")
print("sum: ", sum)
