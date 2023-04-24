# 1. Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def ComputePay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    return pay


hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
print("Pay: " + str(ComputePay(hours, rate)))
