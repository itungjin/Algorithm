# DFS, BFS
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())  # 3 <= n, m <= 8
data = [list(map(int, input().split())) for _ in range(n)]

answer = 0
viruses = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            viruses.append([i, j])


def block(r, c, count):
    count -= 1
    data[r][c] = 1

    if count != 0:
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    block(i, j, count)
    else:
        global answer
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        _data = deepcopy(data)
        for i, j in viruses:
            queue = deque([[i, j]])
            _data[i][j] = 2
            while queue:
                i, j = queue.popleft()
                for di, dj in moves:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if _data[ni][nj] == 0:
                            _data[ni][nj] = 2
                            queue.append([ni, nj])
        safety_area = 0
        for i in range(n):
            safety_area += _data[i].count(0)
        answer = max(answer, safety_area)
    data[r][c] = 0


for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            block(i, j, 3)

print(answer)
