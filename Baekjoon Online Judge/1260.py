import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N + 1):
    graph[i].sort(reverse = True)
visited = [False] * (N + 1)
s = [V]
while s:
    v = s.pop()
    if visited[v]:
        continue
    visited[v] = True
    print(v, end=' ')
    for u in graph[v]:
        if not visited[u]:
            s.append(u)
print()
for i in range(1, N + 1):
    graph[i].sort()
visited = [False] * (N + 1)
q = deque([V])
print(V, end=' ')
visited[V] = True
while q:
    v = q.popleft()
    for u in graph[v]:
        if not visited[u]:
            q.append(u)
            print(u, end=' ')
            visited[u] = True
print()
