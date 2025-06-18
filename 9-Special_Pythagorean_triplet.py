for a in range(1, 999):
    for b in range(1, 1000-a):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a, b, c)
            print(a*b*c)

# 200 375 425
# 31875000
# 375 200 425
# 31875000
# [Finished in 0.429s]
