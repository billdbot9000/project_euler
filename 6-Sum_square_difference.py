
N = 100
sumDifference = int(N * (N + 1) / 2)
sumDifference = sumDifference*sumDifference

for i in range(1, 101):
    sumDifference = sumDifference - i * i

print(sumDifference)
