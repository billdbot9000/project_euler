collatz_length = dict()
collatz_length[1] = 1
maxSeq = (1, 1)

for start in range(2, 1000000):
    n = start
    count = 1
    while start not in collatz_length:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1

        if n in collatz_length:
            collatz_length[start] = collatz_length[n] + count
        else:
            count = count + 1

    if collatz_length[start] > maxSeq[1]:
        maxSeq = (start, collatz_length[start])

print(maxSeq)

# (837799, 525)
# [Finished in 3.841s]
