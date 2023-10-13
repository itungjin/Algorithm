import sys
from collections import deque

input = sys.stdin.readline

t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    count = 0
    for i in range(1, n + 1):
        if parent[i] == 0:
            is_tree = True
            q = deque([i])
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if nxt == parent[cur]:
                        continue
                    if parent[nxt] == 0:
                        q.append(nxt)
                        parent[nxt] = cur
                    else:
                        is_tree = False
            if is_tree:
                count += 1
    print(f'Case {t}: ', end='')
    if count > 1:
        print(f'A forest of {count} trees.')
    elif count == 1:
        print('There is one tree.')
    else:
        print('No trees.')
