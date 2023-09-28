import sys
from collections import deque

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input().rstrip())
boxes = [list(map(int, input().split())) for _ in range(M)]
boxes.sort(key=lambda x: (x[1], x[0]))
answer = 0
capacity = [0] * (N + 1)
for f, t, c in boxes:
    max_c = C - max(capacity[f:t])
    if c < max_c:
        max_c = c
    answer += max_c
    for i in range(f, t):
        capacity[i] += max_c
print(answer)