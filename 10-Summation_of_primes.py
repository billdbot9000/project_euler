import math


# checks if the input number is prime, returns True or False
def IsPrime(candidatePrime):
    i = 2
    while i <= math.sqrt(candidatePrime):
        if candidatePrime % i == 0:
            return False
        i = i + 1

    return True


# takes an integer >=2 as input
# returns a list of size limit+1, with a boolean value indicating whether the
# number at that index is prime. I.e. prime_list[7] = True b/c 7 is prime,
# prime_list[6] = False b/c 6 is not prime
# uses the sieve of eratosthenes to generate this list
def FindPrimes(limit):
    prime_list = [True for i in range(0, limit+1)]
    prime_list[0] = False
    prime_list[1] = False

    i = 2
    while i <= math.sqrt(limit):
        if prime_list[i]:
            for j in range(i*i, limit+1, i):
                prime_list[j] = False

        i = i + 1

    return prime_list


# returns the sum of all prime numbers below the input limit
def SumPrimes(limit):
    prime_list = FindPrimes(limit)
    sum = 0
    for i in range(2, limit):
        if prime_list[i]:
            sum = sum + i

    return sum


print(SumPrimes(2000000))

# 142913828922
# [Finished in 53.378s]
# checking each candidate prime

# 142913828922
# [Finished in 0.686s]
# using sieve to generate primes
