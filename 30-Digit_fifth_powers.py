#!/usr/bin/python


def FifthPowerDigitSum(number: int) -> int:
    sum = 0
    for digit in str(number):
        sum += int(digit)**5

    return sum


for i in range(10, 1000000):
    if i == FifthPowerDigitSum(i):
        print(i)

'''
file = open("p030_data.csv", "w")
for i in range(10, 1000000):
    file.write(str(i) + "," + str(FifthPowerDigitSum(i)) + "\n")

file.close()
'''
