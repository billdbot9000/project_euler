import math


def SumDivisors(number):
    sum = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if i*i == number:
                sum += i
            else:
                sum += i
                sum += int(number/i)

    return sum


abundant = set()
for i in range(1, 28112):
    if SumDivisors(i) > i:
        abundant.add(i)

total = 0
for j in range(1, 28123):
    abundantSum = False
    for i in abundant:
        if j - i in abundant:
            abundantSum = True
            break
    if not abundantSum:
        total += j

print(total)
