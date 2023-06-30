# 구현

import sys

input = sys.stdin.readline

N = int(input().strip())

answer = 0
for _ in range(N):
    word = input()

    flag = True
    i = len(word) - 1
    while i >= 0:
        if word.find(word[i]) != i:
            j = i-1
            while j >= word.find(word[i]):
                if word[j] != word[i]:
                    flag = False
                    break
                j -= 1
            i = j
        else:
            i -= 1

        if not flag:
            break

    if flag:
        answer += 1

print(answer)
