# calculate 40 choose 20
def Factorial(number):
    if number == 0:
        return 1
    elif number > 0:
        return number*Factorial(number-1)
    else:
        return 0


paths = 1
for i in range(39, 20, -2):
    paths = paths * i

paths = paths * (2**10)
paths = int(paths/Factorial(10))

print(paths)

# 137846528820
# [Finished in 0.234s]
