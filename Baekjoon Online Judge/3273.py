# 구현

import sys

input = sys.stdin.readline

n = int(input().rstrip())
sequence = list(map(int, input().split()))
x = int(input().rstrip())

answer = 0
count = [0] * 1000001
for num in sequence:
    if x-num <= 1000000 and count[x-num] == 1:
        answer += 1
    count[num] += 1

print(answer)
