def IsPandigitalProduct(mult1, mult2, product_digits):
    product = int(mult1)*int(mult2)
    if ''.join(sorted(str(product))) == ''.join(sorted(product_digits)):
        return True
    else:
        return False


baseSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
n1 = n2 = n3 = n4 = n5 = int()
mults, product_digits, mult1, mult2 = "", "", "", ""
pandigital_set = set()
pan_products = set()
sum = 0

for n1 in baseSet:
    for n2 in baseSet - {n1}:
        for n3 in baseSet - {n1, n2}:
            for n4 in baseSet - {n1, n2, n3}:
                for n5 in baseSet - {n1, n2, n3, n4}:
                    mults = ''.join(str(x) for x in [n1, n2, n3, n4, n5])
                    product_digits = ''.join(str(x)
                                             for x in baseSet - {n1, n2, n3, n4, n5})

                    for sep in 1, 2, 3, 4:
                        mult1 = mults[0:sep]
                        mult2 = mults[sep:]

                        if IsPandigitalProduct(mult1, mult2, product_digits):
                            if int(mult1) < int(mult2):
                                pandigital_set.add(
                                    (int(mult1), int(mult2), int(mult1) * int(mult2)))
                            else:
                                pandigital_set.add(
                                    (int(mult2), int(mult1), int(mult1) * int(mult2)))

                            pan_products.add(int(mult1)*int(mult2))

for panTuple in pandigital_set:
    print(panTuple)

for x in pan_products:
    sum = sum + x

print(sum)
