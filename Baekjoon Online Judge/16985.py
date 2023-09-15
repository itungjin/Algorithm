import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
torb = []
vertex = [(0, 0), (0, 4), (4, 0), (4, 4)]
for x in range(5):
    for y, z in vertex:
        if arr[x][y][z] == 1:
            torb.append(x)


def rotate(board):
    temp = [[0] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            temp[c][4 - r] = board[r][c]
    for r in range(5):
        for c in range(5):
            board[r][c] = temp[r][c]


rotated_arr = [[0] * 4 for _ in range(5)]
for i in range(5):
    for j in range(4):
        if j == 0:
            rotated_arr[i][j] = arr[i]
        else:
            rotated_arr[i][j] = deepcopy(rotated_arr[i][j - 1])
            rotate(rotated_arr[i][j])

answer = 1e9
used = [False] * 5
orders = [0] * 5
records = set()

start = [(0, 0, 0), (0, 0, 4), (0, 4, 0), (0, 4, 4),
         (4, 0, 0), (4, 0, 4), (4, 4, 0), (4, 4, 4)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def escape(b, pos):
    global answer
    x, y, z = start[pos]
    if b[x][y][z] == 0:
        return
    q = deque([(x, y, z)])
    b[x][y][z] = 0
    while q:
        x, y, z = q.popleft()
        if x == start[7 - pos][0] and y == start[7 - pos][1] and z == start[7 - pos][2]:
            answer = min(answer, b[x][y][z])
            return
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if b[nx][ny][nz] == 1:
                    b[nx][ny][nz] = b[x][y][z] + 1
                    q.append((nx, ny, nz))


def solution(n):
    if n == 5:
        record = f'{orders[0]}{orders[1]}{orders[2]}{orders[3]}{orders[4]}'
        record_reverse = f'{orders[4]}{orders[3]}{orders[2]}{orders[1]}{orders[0]}'
        if record in records:
            return
        records.add(record)
        records.add(record_reverse)
        b = [0] * 5
        b[0] = arr[orders[0]]
        for i in range(4):
            b[1] = rotated_arr[orders[1]][i]
            for j in range(4):
                b[2] = rotated_arr[orders[2]][j]
                for k in range(4):
                    b[3] = rotated_arr[orders[3]][k]
                    for l in range(4):
                        b[4] = rotated_arr[orders[4]][l]
                        for m in range(4):
                            escape(deepcopy(b), m)
    else:
        if n == 0 or n == 4:
            for i in range(len(torb)):
                if not used[torb[i]]:
                    orders[n] = torb[i]
                    used[torb[i]] = True
                    solution(n + 1)
                    used[torb[i]] = False
        else:
            for i in range(5):
                if not used[i]:
                    orders[n] = i
                    used[i] = True
                    solution(n + 1)
                    used[i] = False


solution(0)
if answer == 1e9:
    print(-1)
else:
    print(answer)
