from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
distance = [[0] * M for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

q = deque()
q.append((0, 0))
distance[0][0] = 1
while q and distance[N-1][M-1] == 0:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and distance[nr][nc] == 0:
            distance[nr][nc] = distance[r][c] + 1
            q.append((nr, nc))

print(distance[N-1][M-1])