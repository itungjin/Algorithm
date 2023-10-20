import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
K = int(input().rstrip())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dist = [INF] * (V + 1)
dist[K] = 0
heap = [(0, K)]
while heap:
    d, v = heapq.heappop(heap)
    if d != dist[v]:
        continue
    for nv, nw in graph[v]:
        if d + nw < dist[nv]:
            dist[nv] = d + nw
            heapq.heappush(heap, (d + nw, nv))
for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
