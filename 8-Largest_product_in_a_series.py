LongNumberString = "73167176531330624919225119674426574742355349194934"
LongNumberString = LongNumberString + \
    "96983520312774506326239578318016984801869478851843"
LongNumberString = LongNumberString + \
    "85861560789112949495459501737958331952853208805511"
LongNumberString = LongNumberString + \
    "12540698747158523863050715693290963295227443043557"
LongNumberString = LongNumberString + \
    "66896648950445244523161731856403098711121722383113"
LongNumberString = LongNumberString + \
    "62229893423380308135336276614282806444486645238749"
LongNumberString = LongNumberString + \
    "30358907296290491560440772390713810515859307960866"
LongNumberString = LongNumberString + \
    "70172427121883998797908792274921901699720888093776"
LongNumberString = LongNumberString + \
    "65727333001053367881220235421809751254540594752243"
LongNumberString = LongNumberString + \
    "52584907711670556013604839586446706324415722155397"
LongNumberString = LongNumberString + \
    "53697817977846174064955149290862569321978468622482"
LongNumberString = LongNumberString + \
    "83972241375657056057490261407972968652414535100474"
LongNumberString = LongNumberString + \
    "82166370484403199890008895243450658541227588666881"
LongNumberString = LongNumberString + \
    "16427171479924442928230863465674813919123162824586"
LongNumberString = LongNumberString + \
    "17866458359124566529476545682848912883142607690042"
LongNumberString = LongNumberString + \
    "24219022671055626321111109370544217506941658960408"
LongNumberString = LongNumberString + \
    "07198403850962455444362981230987879927244284909188"
LongNumberString = LongNumberString + \
    "84580156166097919133875499200524063689912560717606"
LongNumberString = LongNumberString + \
    "05886116467109405077541002256983155200055935729725"
LongNumberString = LongNumberString + \
    "71636269561882670428252483600823257530420752963450"


# takes a string as input, which is assumes to have only digits as characters
# returns the product of these digits
def DigitProduct(NumberString):
    product = 1
    for i in range(0, len(NumberString)):
        product = product * int(NumberString[i])

    return product


product = int()
maxProduct = 0
maxString = str()
for i in range(0, len(LongNumberString) - 12):
    product = DigitProduct(LongNumberString[i:i+13])
    if product > maxProduct:
        maxProduct = product
        maxString = LongNumberString[i:i+13]

print(maxProduct, maxString)

# 23514624000 5576689664895
# [Finished in 0.117s]
