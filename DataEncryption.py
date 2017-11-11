lines = raw_input()
lines = int(lines)
columns = 7
summ_lst = []
matrix = [[None for x in range(columns)] for y in range(lines)]
while lines != 0:
    number = raw_input().split(' ')
    lst_number = [int(item) for item in number]
    i = 0
    for col in range(columns):
        matrix[lines - 1][col] = lst_number[i]
        i += 1

    lines -= 1

for number in matrix:
    permutations = []
    encryption = []
    for i in range(0, len(number), 2):
        if i == 6:
            permutations.append(number[i])
        else:
            permutations.append(number[i+1])
            permutations.append(number[i])

    for j in range(len(permutations)):
        if j == 0:
            encryption.append(permutations[j])
        else:
            encryption.append(permutations[j] % 2)
    summ_lst.append(sum(encryption))

summ_lst.sort()
print(summ_lst[len(summ_lst) - 1])



