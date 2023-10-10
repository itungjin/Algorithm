import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))
for i in range(N):
    visited = [0] * N
    q = deque([i])
    while q:
        v = q.popleft()
        for j in range(N):
            if graph[v][j] == 1 and visited[j] == 0:
                visited[j] = 1
                q.append(j)
    print(*visited)
