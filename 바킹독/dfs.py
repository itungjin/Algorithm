ROW, COL = 10, 10

visited = [[False] * COL for _ in range(ROW)]
coordinate = [[0] * COL for _ in range(ROW)]
stack = []

def dfs(row, col):
    visited[row][col] = True
    stack.append((row, col))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while stack:
        row, col = stack.pop()
        print(f'({row}, {col})')
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0 <= nx < ROW and 0 <= ny < COL:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

dfs(0, 0)
