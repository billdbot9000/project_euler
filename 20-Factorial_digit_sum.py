def FactorialMod10(n):
    product = 1
    while n > 1:
        product = product*n
        n = n-1
        while product % 10 == 0:
            product //= 10
    return product


digitString = str(FactorialMod10(100))
sum = 0
for i in digitString:
    sum += int(i)

print(sum)
