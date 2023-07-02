# 구현

import sys

input = sys.stdin.readline

words = [[] for _ in range(5)]
max_c = 0
for i in range(5):
    words[i] = list(input().rstrip())
    max_c = max(max_c, len(words[i]))

for c in range(max_c):
    for r in range(5):
        if len(words[r]) > c:
            print(words[r][c], end='')
