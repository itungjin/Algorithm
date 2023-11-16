import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
visited = [False] * (N + 1)
answer = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = True
    answer += 1
    q.append(i)
    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            q.append(v)

print(answer)
