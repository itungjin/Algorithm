import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
grid = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
count = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque()
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            visited[i][j] = True
            color = grid[i][j]
            if color == 'R':
                grid[i][j] = 'G'
            q.append((i, j))
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == color and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        if grid[nr][nc] == 'R':
                            grid[nr][nc] = 'G'
print(count, end=' ')
visited = [[False] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            visited[i][j] = True
            color = grid[i][j]
            q.append((i, j))
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == color and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
print(count)
