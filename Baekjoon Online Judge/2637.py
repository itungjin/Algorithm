import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
need = [dict() for _ in range(N + 1)]
basic = set()
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append(X)
    indegree[X] += 1
    need[X][Y] = K
for i in range(1, N):
    if indegree[i] == 0:
        basic.add(i)
q = deque(basic)
while q:
    v = q.popleft()
    for u in graph[v]:
        indegree[u] -= 1
        if v not in basic:
            for w in need[v]:
                if w in need[u]:
                    need[u][w] += need[v][w] * need[u][v]
                else:
                    need[u][w] = need[v][w] * need[u][v]
            del need[u][v]
        if indegree[u] == 0:
            q.append(u)
basic = sorted(list(basic))
for i in basic:
    print(i, need[N][i])