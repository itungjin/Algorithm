import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2, t = map(int, input().split())
    graph[v1].append((v2, t))
dist = [0] * (N + 1)
for i in range(1, N + 1):
    tmp = [INF] * (N + 1)
    tmp[i] = 0
    heap = [(0, i)]
    while heap:
        t, v = heapq.heappop(heap)
        if t != tmp[v]:
            continue
        for nv, nt in graph[v]:
            if t + nt < tmp[nv]:
                tmp[nv] = t + nt
                heapq.heappush(heap, (t + nt, nv))
    if i != X:
        dist[i] += tmp[X]
    else:
        for j in range(1, N + 1):
            dist[j] += tmp[j]
print(max(dist))
