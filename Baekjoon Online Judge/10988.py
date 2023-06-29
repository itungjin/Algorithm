# 구현

word = input()

flag = True
for i in range(0, len(word) // 2):
    if word[i] == word[-1 - i]:
        continue
    else:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)
