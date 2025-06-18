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


limit = 10000
divisor_sum = dict()
amicable = set()
for i in range(1, limit):
    sum_i = SumDivisors(i)
    if sum_i not in divisor_sum:
        divisor_sum[sum_i] = [i]
    else:
        divisor_sum[sum_i].append(i)

    if sum_i >= limit:
        if SumDivisors(sum_i) == i:
            amicable.add(i)

    if i in divisor_sum:
        for j in divisor_sum[i]:
            if j == sum_i and j != i:
                amicable.add(j)
                amicable.add(i)

amicableSum = 0
for i in amicable:
    amicableSum += i

print(amicableSum)
