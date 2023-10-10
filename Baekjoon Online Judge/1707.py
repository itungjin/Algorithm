import sys
from collections import deque

input = sys.stdin.readline

K = int(input().rstrip())
for _ in range(K):
    V, E = map(int, input().split())
    if V == 1:
        print('YES')
        continue
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 거리가 짝수면 같은 집합에 속할 수 있음
    dist = [-1] * (V + 1)
    is_bipartite = True
    for i in range(1, V + 1):
        if dist[i] != -1:
            continue
        dist[i] = 0
        q = deque([i])
        while q:
            v = q.popleft()
            for u in graph[v]:
                if dist[u] != -1:
                    if dist[u] == dist[v]:
                        is_bipartite = False
                        break
                else:
                    dist[u] = (dist[v] + 1) % 2
                    q.append(u)
            if not is_bipartite:
                break
        if not is_bipartite:
            break
    if is_bipartite:
        print('YES')
    else:
        print('NO')
