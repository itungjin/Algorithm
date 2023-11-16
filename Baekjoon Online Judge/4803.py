import sys
from collections import deque

input = sys.stdin.readline

case = 0
while True:
    case += 1

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    t = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        node = 0
        edge = 0
        q = deque([i])
        while q:
            u = q.popleft()
            node += 1
            for v in graph[u]:
                edge += 1
                if visited[v]:
                    continue
                visited[v] = True
                q.append(v)
        edge //= 2
        if node == edge + 1:
            t += 1

    print(f'Case {case}: ', end='')
    if t == 0:
        print('No trees.')
    elif t == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {t} trees.')
