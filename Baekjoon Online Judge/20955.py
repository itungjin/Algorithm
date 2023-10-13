import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    # 중복 간선 제거
    if v in graph[u]:
        cnt += 1
        continue
    graph[u].add(v)
    graph[v].add(u)
trees = 0
parent = [0] * (N + 1)
for i in range(1, N + 1):
    if parent[i] != 0:
        continue
    trees += 1
    q = deque([i])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt == parent[cur]:
                continue
            elif parent[nxt] != 0:
                cnt += 1
                graph[nxt].remove(cur)
            else:
                q.append(nxt)
                parent[nxt] = cur
cnt += trees - 1
print(cnt)
