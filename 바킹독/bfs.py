from collections import deque

MAX = 502
ROW, COL = 7, 10

visited = [[False] * MAX for _ in range(MAX)]
board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque()

visited[0][0] = True
q.append((0, 0))
while q:
    r, c = q.popleft()
    print(f'({r},{c})')
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc))
