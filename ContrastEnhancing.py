import math
lines = raw_input()
columns = raw_input()
lines = int(lines)
columns = int(columns)
number_of_items = lines * columns

def enhancing_func(pixel):
    enh_pixel = math.floor(((pixel * 0.9) + 2))
    return enh_pixel

matrix = [[0 for x in range(columns)] for y in range(lines)]
for i in range(lines):
    for j in range(columns):
        pixel = raw_input()
        matrix[i][j] = int(pixel)

new_matrix = [[0 for c in range(columns)] for l in range(lines)]

for i in range(lines):
    for j in range(columns):
        new_matrix[i][j] = enhancing_func(matrix[i][j]) - matrix[i][j]
summ = 0
for lst in new_matrix:
    for item in lst:
        summ += item
average = summ/number_of_items

print(round(average, 2))


