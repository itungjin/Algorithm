import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, c = map(int, input().split())
    graph[v1].append((v2, c))
st, en = map(int, input().split())
dist = [INF] * (n + 1)
dist[st] = 0
heap = [(0, st)]
pre = [st] * (n + 1)
while heap:
    c, v = heapq.heappop(heap)
    if c != dist[v]:
        continue
    for nv, nc in graph[v]:
        if c + nc < dist[nv]:
            dist[nv] = c + nc
            pre[nv] = v
            heapq.heappush(heap, (dist[nv], nv))
print(dist[en])
v = en
route = [en]
while v != st:
    v = pre[v]
    route.append(v)
    if v == st:
        break
print(len(route))
for i in range(len(route) -1, -1, -1):
    print(route[i], end=' ')
