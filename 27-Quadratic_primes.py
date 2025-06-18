import math


# checks if the input number is prime, returns True or False
def IsPrime(candidatePrime):
    i = 2
    while i <= math.sqrt(candidatePrime):
        if candidatePrime % i == 0:
            return False
        i = i + 1

    return True


# takes an integer >=2 as input (e.g. limit)
# returns a set with all primes up to that limit
# uses the sieve of eratosthenes to generate this set
def FindPrimes(limit: int) -> set:
    prime_set = set()
    prime_list = [True for i in range(0, limit+1)]
    prime_list[0] = False
    prime_list[1] = False

    i = 2
    while i <= math.sqrt(limit):
        if prime_list[i]:
            for j in range(i*i, limit+1, i):
                prime_list[j] = False

        i = i + 1

    for i in range(0, limit+1):
        if prime_list[i]:
            prime_set.add(i)

    return prime_set


# find all primes <= 1000, store them in a set
prime_set = FindPrimes(1000)
max_tuple = (1, 41, 39)
is_prime_counter = 0
for b in prime_set:
    for a in range(-999, 1000):
        n = 0
        polyprime_n = True
        while polyprime_n:
            n += 1
            polyval = n*n + a*n + b
            if polyval < 1000:
                polyprime_n = polyval in prime_set
            else:
                polyprime_n = IsPrime(polyval)
                is_prime_counter += 1

        if n-1 > max_tuple[2]:
            max_tuple = (a, b, n-1)

print(max_tuple)
print(is_prime_counter)
