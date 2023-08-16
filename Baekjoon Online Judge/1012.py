import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1
    count = 0
    q = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                count += 1
                q.append((r, c))
                while q:
                    row, col = q.popleft()
                    for i in range(4):
                        nr, nc = row + dr[i], col + dc[i]
                        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    print(count)
