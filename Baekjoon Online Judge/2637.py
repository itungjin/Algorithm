import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
cnt = [0] * (N + 1)
cnt[N] = 1
is_basic = [True] * (N + 1)
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    indegree[Y] += 1
    is_basic[X] = False
q = deque([N])
while q:
    v = q.popleft()
    for u, k in graph[v]:
        indegree[u] -= 1
        cnt[u] += k * cnt[v]
        if indegree[u] == 0:
            q.append(u)
for i in range(1, N + 1):
    if is_basic[i]:
        print(i, cnt[i])
