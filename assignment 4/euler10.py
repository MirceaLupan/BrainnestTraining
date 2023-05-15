# A unit fraction contains 1 in the numerator. The decimal representation
# of the unit fractions with denominators 2 to 10 are given:
# 1/2     =       0.5
# 1/3     =       0.(3)
# 1/4     =       0.25
# 1/5     =       0.2
# 1/6     =       0.1(6)
# 1/7     =       0.(142857)
# 1/8     =       0.125
# 1/9     =       0.(1)
# 1/10    =       0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.


def check(d, nums, rems, quotients):
    """Check if 1/d contain recurring cycle and store decimal fraction part in quotients"""
    l = len(nums)
    for i in range(l - 2, -1, -1):
        if nums[i] == nums[l - 1] and rems[i] == rems[l - 1]:
            quotients[d] = [l - i - 1,
                            "".join([str(x) for x in nums[0:i]]),
                            "".join([str(x) for x in nums[i:l - 1]])]
            return True
    return False


quotients = dict()

for den in range(2, 1000):
    rem = 1
    nums = []
    rems = []
    while rem:
        num = rem * 10
        rem = num % den
        num //= den
        nums.append(num)
        rems.append(rem)
        if check(den, nums, rems, quotients):
            break

# print all numbers with recurring cycle
for key, value in quotients.items():
    print(f"d = {key}, length = {value[0]}    1/d = 0.{value[1]}({value[2]})")

# print the number with the largest recurring cycle
print("\nThe largest recurring cycle:")
key = max(quotients, key=quotients.get)
print(f"d = {key}, length = {quotients[key][0]}    1/d = 0.{quotients[key][1]}({quotients[key][2]})")
