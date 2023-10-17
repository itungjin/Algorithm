import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in range(2, len(tmp)):
        graph[tmp[j]].append(i)
    indegree[i] = tmp[1]
heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, (time[i], i))
now = 0
while heap:
    now, v = heapq.heappop(heap)
    for u in graph[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            heapq.heappush(heap, (now + time[u], u))
print(now)
