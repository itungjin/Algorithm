import sys
from collections import deque

input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]
N = int(input().rstrip())  # board의 크기
K = int(input().rstrip())  # 사과의 개수
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = -1
L = int(input().rstrip())  # 방향 변환 횟수
turn = [0] * L
for i in range(L):
    X, C = input().split()
    turn[i] = (int(X), C)

r, c = 0, 0
time = 0
turn_idx = 0
d = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
board[0][0] = 1
q = deque([(0, 0)])
while True:
    time += 1
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < N and 0 <= nc < N:
        if board[nr][nc] == 0:
            board[nr][nc] = 1
            q.append((nr, nc))
            tr, tc = q.popleft()
            board[tr][tc] = 0
            r, c = nr, nc
        elif board[nr][nc] == -1:
            board[nr][nc] = 1
            q.append((nr, nc))
            r, c = nr, nc
        else:
            break
    else:
        break
    if turn_idx < L:
        if turn[turn_idx][0] == time:
            if turn[turn_idx][1] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            turn_idx += 1
print(time)
