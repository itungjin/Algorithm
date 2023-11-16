import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [set() for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
for i in range(1, N + 1):
    graph[i] = sorted(list(graph[i]))


visited = [False] * (N + 1)
visited[V] = True


def dfs(u):
    print(u, end=' ')
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v)


visited[V] = True
dfs(V)
print()


def bfs(u):
    visited = [False] * (N + 1)
    visited[u] = True
    q = deque([u])
    while q:
        u = q.popleft()
        print(u, end=' ')
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


bfs(V)

