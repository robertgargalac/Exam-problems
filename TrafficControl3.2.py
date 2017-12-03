n = raw_input()
bus_numbers = raw_input()
n = int(n)
missed = []
numbers = bus_numbers.split(' ')
b_numbers = []
for num in numbers:
    try:
        num = int(num)
        b_numbers.append(num)
    except:
        b_numbers.append(0)

all_numbers = list(xrange(1, n + 1, 1))

for number in all_numbers:
    if number in b_numbers:
        continue
    else:
        missed.append(number)
summ = 0
for item in missed:
    summ += item

print(summ)