from __future__ import division

c, k, n = raw_input().split(' ')
list_of_packages = raw_input().split(' ')
k = int(k)
n = int(n)
packages_vect = [int(item) for item in list_of_packages]
columns = n//k + 1
#columns = int(round(n/k))
#if columns < 1:
    #columns = 1
Matrix = [[None for x in range(columns)] for y in range(k)]
i = 0
items_left = len(packages_vect)
for col in range(columns):
    for line in range(k):
        if items_left == 0:
            break
        Matrix[line][col] = packages_vect[i]
        items_left -= 1
        i += 1
for item in Matrix:
    item = str(item)
    item = item.replace('[', '')
    item = item.replace(']', '')
    item = item.replace(',', '')
    item = item.replace('None', '')
    print(item)








