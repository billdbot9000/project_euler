import math


def CountDivisors(positiveInteger):
    count = 0
    for i in range(1, math.floor(math.sqrt(positiveInteger)) + 1):
        if positiveInteger % i == 0:
            if i*i == positiveInteger:
                count = count + 1
            else:
                count = count + 2

    return count


# find the first triangular number with >500 divisors
# triangular numbers should all have the form n*(n+1)/2 (for positive int n)
n = 0
numDivisors = 0

while numDivisors <= 500:
    n = n + 1
    numDivisors = CountDivisors(int(n*(n+1)/2))

print(n, int(n*(n+1)/2), numDivisors)

# 12375 76576500 576
# [Finished in 4.205s]
