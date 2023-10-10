import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0
for u in range(1, N + 1):
    if visited[u]:
        continue
    q = deque([u])
    while q:
        now = q.popleft()
        for v in graph[now]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    count += 1
print(count)
