import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)
parent[1] = 0
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
q = deque([1])
while q:
    p = q.popleft()
    for c in graph[p]:
        if parent[c] == -1:
            parent[c] = p
            q.append(c)
for i in range(2, N + 1):
    print(parent[i])
