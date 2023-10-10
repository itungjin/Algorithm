import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    stations = list(map(int, input().split()))
    for i in range(len(stations)):
        for j in range(i, len(stations)):
            graph[stations[i]].append(stations[j])
            graph[stations[j]].append(stations[i])
distance = [-1] * (N + 1)
distance[1] = 1
q = deque([1])
while q:
    v = q.popleft()
    for u in graph[v]:
        if distance[u] == -1:
            distance[u] = distance[v] + 1
            q.append(u)
print(distance[N])
