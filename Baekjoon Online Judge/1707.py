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
    visited = [False] * (V + 1)
    is_bipartite = True
    for i in range(1, V + 1):
        if visited[i]:
            continue
        visited[i] = True
        belong = {i: 1}
        q = deque([i])
        while q:
            v = q.popleft()
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
                    if belong[v] == 1:
                        belong[u] = 2
                    else:
                        belong[u] = 1
        for v in belong.keys():
            for u in graph[v]:
                if belong[v] == belong[u]:
                    is_bipartite = False
                    break
            if not is_bipartite:
                break
        if not is_bipartite:
            break
    if is_bipartite:
        print('YES')
    else:
        print('NO')
