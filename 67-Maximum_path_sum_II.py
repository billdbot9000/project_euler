#!/usr/bin/python

'''
pyramid = [[3],
           [7, 4],
           [2, 4, 6],
           [8, 5, 9, 3]]
'''
file = open('p067_triangle.txt', 'r')

line = str()
pyramid = list()
row = 0
for line in file:
    line = line.replace("\n", "")
    pyramid.append(line.split(" "))
    pyramid[row] = [int(i) for i in pyramid[row]]
    row += 1

maxsums = dict()
bottom_row = len(pyramid)-1
for i in range(0, len(pyramid[bottom_row])):
    maxsums[(bottom_row, i)] = (pyramid[bottom_row][i], "")

for i in range(bottom_row-1, -1, -1):
    for j in range(0, len(pyramid[i])):
        if maxsums[(i+1, j)][0] > maxsums[(i+1, j+1)][0]:
            maxsums[(i, j)] = (pyramid[i][j] + maxsums[(i+1, j)][0],
                               "0" + maxsums[(i+1, j)][1])
        else:
            maxsums[(i, j)] = (pyramid[i][j] + maxsums[(i+1, j+1)][0],
                               "1" + maxsums[(i+1, j+1)][1])

print(maxsums[(0, 0)])
