#!/usr/bin/python


current = sum = 1
for side_length in range(3, 1002, 2):
    for i in range(0, 4):
        current += side_length - 1
        sum += current

print(sum)
