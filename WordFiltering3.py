sentence = raw_input()
number_forbiden_words = raw_input()
number_forbiden_words = int(number_forbiden_words)
forbiden_words = raw_input().split(' ')
refact_sentence = []

for word in forbiden_words:
    sentence = sentence.replace(word, len(word) * '*')

print(sentence)

