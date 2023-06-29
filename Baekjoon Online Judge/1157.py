# 구현

word = input()

count = dict()
for i in range(ord('A'), ord('Z') + 1):
    count[chr(i)] = [0, i]

for char in word:
    if ord(char) > ord('Z'):
        char = chr(ord(char) - (ord('a') - ord('A')))
    count[char] = [count[char][0] + 1, char]

count = list(count.values())
count.sort(reverse=True)

if len(word) == 1:
    print(count[0][1])
elif count[0][0] == count[1][0]:
    print('?')
else:
    print(count[0][1])
