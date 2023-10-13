import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2, dist = map(int, input().split())
    graph[v1].append((v2, dist))
    graph[v2].append((v1, dist))

for _ in range(M):
    v1, v2 = map(int, input().split())
    q = deque([v1])
    dists = [-1] * (N + 1)
    dists[v1] = 0
    while q:
        cur = q.popleft()
        for nxt, dist in graph[cur]:
            if dists[nxt] != -1:
                continue
            q.append(nxt)
            dists[nxt] = dists[cur] + dist
            if nxt == v2:
                q.clear()
                break
    print(dists[v2])
