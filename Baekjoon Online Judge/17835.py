import sys
import heapq

INF = int(1e10)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [dict() for _ in range(N + 1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    if U in graph[V]:
        if C < graph[V][U]:
            graph[V][U] = C
    else:
        graph[V][U] = C
interview = list(map(int, input().split()))

distance = [INF] * (N + 1)
heap = []
for city in interview:
    distance[city] = 0
    heapq.heappush(heap, (0, city))
while heap:
    dist, city = heapq.heappop(heap)
    if distance[city] != dist:
        continue
    for U in graph[city].keys():
        C = graph[city][U]
        if dist + C < distance[U]:
            distance[U] = dist + C
            heapq.heappush(heap, (distance[U], U))
farthest = 0
farthest_city = 1
for i in range(1, N + 1):
    if distance[i] > farthest:
        farthest = distance[i]
        farthest_city = i
print(farthest_city)
print(farthest)
