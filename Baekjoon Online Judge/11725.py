import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
parent = [0] * (N + 1)
parent[1] = -1
q = deque([1])
while q:
    u = q.popleft()
    for v in graph[u]:
        if parent[v] == 0:
            parent[v] = u
            q.append(v)

for i in range(2, N + 1):
    print(parent[i])
