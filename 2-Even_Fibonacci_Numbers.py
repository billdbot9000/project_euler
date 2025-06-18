#!/usr/bin/python

first = 1
second = 2
sum = 2
temp = first + second
while temp < 4000000:
    if temp % 2 == 0:
        sum = sum + temp

    first = second
    second = temp
    temp = first + second

print(sum)
