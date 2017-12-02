import string
text = raw_input()
pairs = raw_input()
reconstruct = ''
rcn_list = []
list_pairs = pairs.split(" ")
tokenized = list(text)
punctuation = string.punctuation + ' '

for i in range(len(tokenized)):
    if tokenized[i] in punctuation:
        continue
    for pair in list_pairs:

        actual_char, encoding = pair.split(",")
        if tokenized[i] == actual_char:
            tokenized[i] = encoding
            break
        else:
            continue
for item in tokenized:
    reconstruct += item
print(reconstruct)

