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
s = []

visited[0][0] = True
s.append((0, 0))
while s:
    r, c = s.pop()
    print(f'({r},{c})')
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            s.append((nr, nc))
