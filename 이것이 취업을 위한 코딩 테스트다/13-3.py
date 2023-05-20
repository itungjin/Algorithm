# BFS

import sys
from collections import deque

# 1 <= n <= 200, 1 <= k <= 1000
# n은 시험관의 크기(nXn), k는 바이러스의 종류의 가짓수
n, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# s초 뒤 data[x - 1][y - 1]의 값을 구해야 함
s, x, y = map(int, sys.stdin.readline().split())

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

queue = []
for r in range(n):
    for c in range(n):
        if data[r][c] != 0:
            queue.append([data[r][c], 0, r, c])

queue.sort()
queue = deque(queue)

while queue:
    virus, _s, r, c = queue.popleft()
    if _s == s:
        break
    for mr, mc in moves:
        nr, nc = r + mr, c + mc
        if 0 <= nr < n and 0 <= nc < n and data[nr][nc] == 0:
            data[nr][nc] = virus
            queue.append([virus, _s + 1, nr, nc])

answer = data[x - 1][y - 1]
print(answer)
