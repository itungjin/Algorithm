# 구현

word = input()

word = word.upper()

count = [0] * (ord('Z') + 1)
answer = ''
most_repeated = 0

for char in word:
    count[ord(char)] += 1
    if count[ord(char)] > most_repeated:
        answer = char
        most_repeated += 1
    elif count[ord(char)] == most_repeated:
        answer = '?'

print(answer)
