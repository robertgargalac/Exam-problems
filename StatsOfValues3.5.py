import math
lines = raw_input()
columns = raw_input()
lines = int(lines)
columns = int(columns)
number_values = lines * columns
items = []
hist = []
summ = 0
for _ in range(number_values):
    items.append(int(raw_input()))
unique_items = list(range(10))

for unique_item in unique_items:
    count = 0
    for item in items:
        if item == unique_item:
            count += 1
        else:
            continue
    hist.append(count)

for item in hist:
    summ += item

average = summ/len(hist)
square_err = [hst - average for hst in hist]
square_err_summ = sum(square_err)
average_square_err = math.sqrt(square_err_summ/10)

items_bigger_than_error = [hst for hst in hist if hst > average_square_err]
print(len(items_bigger_than_error))

