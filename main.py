n, k = input().split(' ')
n_vect = input().split(' ')
k_vect = input().split(' ')

n_vect_int = []
k_vect_int = []
n_copy = []

for item1 in n_vect:
    n_vect_int.append(int(item1))

for item2 in k_vect:
    k_vect_int.append(int(item2))
k_vect_int = set(k_vect_int)

for i in range(len(n_vect_int)):
    for item in k_vect_int:
        if n_vect_int[i] == item:
            n_copy.append(n_vect_int[i])

for j in range(len(n_copy)):

    for item in n_vect_int:
        counter = 0
        if n_copy[j] == item:
            n_vect_int.pop(counter)
        counter += 1
        if len(n_vect_int) == 0:
            print('BINGO!')
if len(n_vect_int) > 0:
    print(len(n_vect_int))


