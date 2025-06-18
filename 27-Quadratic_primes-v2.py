import math


# checks if the input number is prime, returns True or False
def IsPrime(candidatePrime: int):
    if candidatePrime < 2:
        return False
    i = 2
    while i <= math.sqrt(candidatePrime):
        if candidatePrime % i == 0:
            return False
        i = i + 1

    return True


# takes an integer >=2 as input
# returns a list of size limit+1, with a boolean value indicating whether the
# number at that index is prime. I.e. prime_list[7] = True b/c 7 is prime,
# prime_list[6] = False b/c 6 is not primes
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


# find all primes <= limit, store them in a set
limit = 10000
prime_list = FindPrimes(limit)
max_tuple = (1, 41, 39)
for b in range(2, 1000):
    if not prime_list[b]:
        continue
    for a in range(-999, 1000):
        n = 0
        polyprime_n = True
        while polyprime_n:
            n += 1
            polyval = n*n + a*n + b
            if polyval >= 0 and polyval <= limit:
                polyprime_n = prime_list[polyval]
            else:
                polyprime_n = IsPrime(polyval)

        if n-1 > max_tuple[2]:
            max_tuple = (a, b, n-1)

print(max_tuple)
