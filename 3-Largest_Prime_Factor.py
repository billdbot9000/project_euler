#!/usr/bin/python

import math


def IsPrime(candidateNumber):
    testDivisor = 2
    while testDivisor < math.sqrt(candidateNumber):
        if candidateNumber % testDivisor == 0:
            return False
        testDivisor = testDivisor + 1

    return True


targetNumber = 600851475143
testDivisor = 2
primeFactors = []
largerFactor = 0

while testDivisor < math.sqrt(targetNumber):
    largerFactor = int(targetNumber / testDivisor)
    if largerFactor * testDivisor == targetNumber:
        if IsPrime(testDivisor):
            primeFactors.append(testDivisor)

        if IsPrime(largerFactor):
            primeFactors.append(largerFactor)

    testDivisor = testDivisor + 1

print(primeFactors)
