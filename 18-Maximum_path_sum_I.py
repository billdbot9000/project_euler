#!/usr/bin/python


file = open('p018_number_pyramid.txt', 'r')

line = str()
pyramid = list()
row = 0
for line in file:
    line = line.replace("\n", "")
    pyramid.append(line.split(" "))
    pyramid[row] = [int(i) for i in pyramid[row]]
    row += 1

extsums = [(0, 0) for i in range(0, len(pyramid))]
for i in range(len(pyramid)-1, -1, -1):
    min = max = pyramid[i][0]
    for j in range(1, len(pyramid[i])):
        if pyramid[i][j] < min:
            min = pyramid[i][j]
        elif pyramid[i][j] > max:
            max = pyramid[i][j]

    if i == len(pyramid)-1:
        extsums[i] = (min, max)
    else:
        extsums[i] = (min + extsums[i+1][0], max + extsums[i+1][1])

pathsums = dict()
pathsums[(0, 0)] = (pyramid[0][0], "")
maxsum = pyramid[0][0]
for row in range(1, len(pyramid)):
    prune = set()
    for elem in pathsums:
        if pathsums[elem][0]+extsums[row][1] < maxsum+extsums[row][0]:
            prune.add(elem)

    for elem in prune:
        pathsums.pop(elem)

    nextrow = dict()
    maxsum = 0
    for currentpos in pathsums:
        for j in 0, 1:
            nextpos = currentpos[1]+j
            nextval = pathsums[currentpos][0] + pyramid[row][nextpos]
            if (row, nextpos) not in nextrow or nextval > nextrow[(row, nextpos)][0]:
                nextrow[(row, nextpos)] = (
                        nextval, pathsums[currentpos][1] + str(j))

            if nextval > maxsum:
                maxsum = nextval

    pathsums = nextrow

max_element = ((0, 0), pyramid[0][0], "")
for elem in pathsums:
    if pathsums[elem][0] > max_element[1]:
        max_element = (elem, pathsums[elem][0], pathsums[elem][1])

print(max_element)
