import math


possible_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms_remaining = 999999
digits = []
j = 0
for i in range(9, 0, -1):
    digits.append(perms_remaining // math.factorial(i))

    perms_remaining -= digits[j]*math.factorial(i)
    j += 1

# print(digits)
next_permutation = str()
for i in range(9):
    # print(digits[i], possible_digits, sep=":")
    next_permutation = next_permutation + str(possible_digits[digits[i]])
    possible_digits.remove(possible_digits[digits[i]])

next_permutation = next_permutation + str(possible_digits[0])
print(next_permutation)
