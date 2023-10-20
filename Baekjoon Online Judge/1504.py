import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        c, v = heapq.heappop(heap)
        if dist[v] != c:
            continue
        for nv, nc in graph[v]:
            tmp = c + nc
            if tmp < dist[nv]:
                dist[nv] = tmp
                heapq.heappush(heap, (tmp, nv))
    return dist[end]


v1_to_v2 = dijkstra(v1, v2)
v2_to_v1 = dijkstra(v2, v1)
st_to_v1 = dijkstra(1, v1)
st_to_v2 = dijkstra(1, v2)
v1_to_en = dijkstra(v1, N)
v2_to_en = dijkstra(v2, N)
ans = min(st_to_v1 + v1_to_v2 + v2_to_en, st_to_v2 + v2_to_v1 + v1_to_en)
if ans >= INF:
    print(-1)
else:
    print(ans)
