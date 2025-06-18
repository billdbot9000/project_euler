#!/usr/bin/python


file = open('p011_grid.txt', 'r')

line = str()
grid_array = list()
row = 0
for line in file:
    line = line.replace("\n", "")
    grid_array.append(line.split(" "))
    grid_array[row] = [int(i) for i in grid_array[row]]
    row += 1

max_product = ((0, 0), (0, 0), (0, 0), (0, 0), 0)
# vertical lines
for i in range(0, len(grid_array) - 3):
    for j in range(0, len(grid_array[i])):
        product = grid_array[i][j] * grid_array[i+1][j] * \
            grid_array[i+2][j] * grid_array[i+3][j]
        if product > max_product[4]:
            max_product = ((i, j), (i+1, j), (i+2, j), (i+3, j), product)

# horizontal lines
for i in range(0, len(grid_array)):
    for j in range(0, len(grid_array[i])-3):
        product = grid_array[i][j] * grid_array[i][j+1] * \
            grid_array[i][j+2] * grid_array[i][j+3]
        if product > max_product[4]:
            max_product = ((i, j), (i, j+1), (i, j+2), (i, j+3), product)

# upper left-lower right diagonals
for i in range(0, len(grid_array)-3):
    for j in range(0, len(grid_array[i])-3):
        product = grid_array[i][j] * grid_array[i+1][j+1] * \
            grid_array[i+2][j+2] * grid_array[i+3][j+3]
        if product > max_product[4]:
            max_product = ((i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3), product)

# lower left-upper right diagonals
for i in range(3, len(grid_array)):
    for j in range(0, len(grid_array[i])-3):
        product = grid_array[i][j] * grid_array[i-1][j+1] * \
            grid_array[i-2][j+2] * grid_array[i-3][j+3]
        if product > max_product[4]:
            max_product = ((i, j), (i-1, j+1), (i-2, j+2), (i-3, j+3), product)

print(max_product)
