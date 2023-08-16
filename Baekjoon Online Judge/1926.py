import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [0] * n
for i in range(n):
    paper[i] = list(map(int, input().split()))

image = 0
max_area = 0
area = 0
visited = [[False] * m for _ in range(n)]
q = deque()
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for r in range(n):
    for c in range(m):
        if paper[r][c] == 1 and not visited[r][c]:
            image += 1
            visited[r][c] = True
            q.append((r, c))
            while q:
                row, col = q.popleft()
                area += 1
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if 0 <= nr < n and 0 <= nc < m and paper[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            max_area = max(max_area, area)
            area = 0

print(image)
print(max_area)