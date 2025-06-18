#!/usr/bin/python

import math

"""
 a couple of approaches:
    - start from factors. each factor is a 3 digit number (ie >=100 and <1000).
        for each product, check if it's a palindrome.
        palindromes should have the form
        [1][2]...[floor(n/2)][floor(n/2)]...[2][1]
        for n digit even numbers and
        [1][2]...[floor(n/2)][floor(n/2)+1][floor(n/2)]...[2][1]
        for n digit odd numbers, where [x] are the digits of some smaller
        "base number" with ceiling(n/2) digits
        each factor has ~10^3 possiblilities, for ~10^6 total products to check
        in this way.
    - start from palindromes. any candidate palindrome is a product of 3 digit
        numbers (>=100 and <1000), so must be 5-6 digits (>=10,000 and
        <1,000,000). "base numbers" for these palindrome would be 3 digits
        (>=100 and <1000). for each palindrome base, construct the palindrome
        then check if it's a product of 3 digit numbers.
        ~10^4 palindrome bases to check
"""


def IsPalindrome(candidateNumber):
    """
    digit_list = []
    totalDigits = math.floor(math.log10(candidateNumber)) + 1
    for i in range(totalDigits - 1, -1, -1):
        digit_list.append(math.floor(candidateNumber / 10 ** i) % 10)

    middleDigit = math.floor(totalDigits / 2)
    for i in range(0, middleDigit):
        if digit_list[i] != digit_list[totalDigits - i - 1]:
            return False

    return True
    """
    stringNumber = str(candidateNumber)
    if stringNumber == stringNumber[::-1]:
        return True
    else:
        return False


product = 0
palindromes = []
maxProduct = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if IsPalindrome(product):
            palindromes.append((product, i, j))
            if product > maxProduct:
                maxProduct = product
                maxProductTuple = (product, i, j)

# print(palindromes)
print(maxProductTuple)
