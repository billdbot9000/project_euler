
# Python program to demonstrate Basic Euclidean Algorithm
# Function to return gcd of a and b


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


product = 1
commonDivisor = 0
for i in range(2, 21):
    commonDivisor = gcd(product, i)
    print(i, product, commonDivisor)

    product = int(product * i / commonDivisor)

print(product)
