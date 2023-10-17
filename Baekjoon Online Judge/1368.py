import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
W = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
graph[0] = [0] * (N + 1)
for i in range(1, N + 1):
    tmp = int(input().rstrip())
    graph[i].append(tmp)
    graph[0][i] = tmp
for i in range(1, N + 1):
    graph[i].extend(list(map(int, input().split())))
heap = []
for i in range(1, N + 1):
    heapq.heappush(heap, (graph[0][i], 0, i))
visited = [False] * (N + 1)
visited[0] = True
cost_sum = 0
cnt = 0
while cnt < N:
    cost, v1, v2 = heapq.heappop(heap)
    if visited[v2]:
        continue
    visited[v2] = True
    cost_sum += cost
    cnt += 1
    for i in range(0, N + 1):
        if not visited[i]:
            heapq.heappush(heap, (graph[v2][i], v2, i))
print(cost_sum)

