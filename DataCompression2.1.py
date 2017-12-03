number_of_lines = raw_input()
number_of_lines = int(number_of_lines)
input_numbers = []
output_numbers = []

while number_of_lines != 0:
    numbers = raw_input()
    input_line = [int(num) for num in numbers.split(',')]
    input_numbers.append(input_line)
    number_of_lines -= 1

for line in input_numbers:
    output_line = []
    counter = 0
    for i in range(len(line)):
        if line[i] == 0:
            counter += 1
        try:
            if line[i] != 0 and line[i + 1] != 0:
                output_line.append(line[i])
                output_line.append(',')
        except:
            if line[i] != 0:
                output_line.append(line[i])


        try:
            if line[i] != 0 and line[i + 1] == 0:
                output_line.append('(')
                output_line.append(line[i])
                output_line.append(',')
        except:
            counter = 0


        try:
            if line[i] == 0 and line[i + 1] != 0:
                output_line.append(counter)
                output_line.append(')')
                output_line.append(',')
                counter = 0
        except:
            if line[i] == 0:
                output_line.append(counter)
                output_line.append(')')
    output_numbers.append(output_line)

for line in output_numbers:
    final = ''
    for i in range(len(line)):

        final += str(line[i])
    print(final)
