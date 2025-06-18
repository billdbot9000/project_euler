#!/usr/bin/python


file = open('p013_50digitnumbers.txt', 'r')

line = str()
sum = 0
for line in file:
    line = line.replace("\n", "")
    sum += int(line)

print(str(sum)[0:10])
