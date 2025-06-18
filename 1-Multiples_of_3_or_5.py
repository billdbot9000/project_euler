#!/usr/bin/python

# sum the multiples of 3 between 0 and 1000, if they aren't multiples of 5
sum = 0
for num in range(3, 1000, 3):
    if num % 5 != 0:
        sum = sum + num

# add in the multiples of 5 between 0 and 1000
# 5 + 10 + ... + 995 = 5*(1 + 2 + ... + 199)
#                    = 5*(199*200/2)
#                    = 99500
sum = sum + 99500

print(sum)
