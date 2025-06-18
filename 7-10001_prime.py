import math


def IsPrime(candidatePrime):
    i = 2
    while i <= math.sqrt(candidatePrime):
        if candidatePrime % i == 0:
            return False
        i = i + 1

    return True


def ListPrimes(N):
    counter = 0
    j = 2
    while True:
        if IsPrime(j):
            counter = counter + 1
            if counter == N:
                return j
        j = j + 1


print(ListPrimes(10001))
