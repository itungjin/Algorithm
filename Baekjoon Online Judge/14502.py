import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
wall = [0] * 3
virus = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            virus.append((r, c))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    global answer
    b = deepcopy(board)
    for r, c in wall:
        b[r][c] = 1
    q = deque()
    for r, c in virus:
        q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if b[nr][nc] == 0:
                    b[nr][nc] = 2
                    q.append((nr, nc))
    temp = 0
    for r in range(N):
        for c in range(M):
            if b[r][c] == 0:
                temp += 1
    answer = max(answer, temp)


def solution(n, r, c):
    if n == 3:
        bfs()
        return
    for nc in range(c + 1, M):
        if board[r][nc] == 0:
            wall[n] = (r, nc)
            solution(n + 1, r, nc)
    for nr in range(r + 1, N):
        for nc in range(M):
            if board[nr][nc] == 0:
                wall[n] = (nr, nc)
                solution(n + 1, nr, nc)


solution(0, 0, -1)
print(answer)
