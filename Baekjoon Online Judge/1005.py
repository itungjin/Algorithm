import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input().rstrip())
    heap = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, (D[i - 1], i))
    now = 0
    v = 0
    while v != W:
        now, v = heapq.heappop(heap)
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                heapq.heappush(heap, (now + D[u - 1], u))
    print(now)
