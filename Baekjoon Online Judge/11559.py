from collections import deque

ROW = 6
COL = 12

board = [list(input()) for _ in range(COL)]
tmp = [['.'] * COL for _ in range(ROW)]
for r in range(ROW):
    for c in range(COL):
        tmp[r][c] = board[c][r]
board = tmp

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(r: int, c: int):
    color = board[r][c]
    count = 0

    connected = []
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        connected.append((r, c))
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == color and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))
                count += 1
    if count >= 4:
        for r, c in connected:
            board[r][c] = '.'
        return True
    return False


def fall(r):
    tmp = ['.'] * COL
    i = COL - 1
    for c in range(COL - 1, -1, -1):
        if board[r][c] != '.':
            tmp[i] = board[r][c]
            i -= 1
    board[r] = tmp


answer = 0
while True:
    is_popped = False
    visited = [[False] * COL for _ in range(ROW)]
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] != '.' and not visited[r][c]:
                if bfs(r, c):
                    is_popped = True
    if is_popped:
        answer += 1
        for r in range(ROW):
            fall(r)
    else:
        break
print(answer)
