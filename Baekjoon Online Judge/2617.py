import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, (input().split()))
graph_heavy_to_light = [set() for _ in range(N + 1)]
graph_light_to_heavy = [set() for _ in range(N + 1)]
for _ in range(M):
    heavy, light = map(int, input().split())
    graph_heavy_to_light[heavy].add(light)
    graph_light_to_heavy[light].add(heavy)

answer = 0
for i in range(1, N + 1):
    count = 0
    visited = [False] * (N + 1)
    q = deque([i])
    while q:
        v = q.popleft()
        for u in graph_heavy_to_light[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
                count += 1
    if count > N // 2:
        answer += 1

for i in range(1, N + 1):
    count = 0
    visited = [False] * (N + 1)
    q = deque([i])
    while q:
        v = q.popleft()
        for u in graph_light_to_heavy[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
                count += 1
    if count > N // 2:
        answer += 1

print(answer)
