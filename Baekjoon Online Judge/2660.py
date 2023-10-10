import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
while True:
    u, v = map(int, input().split())
    if u == - 1 and v == -1:
        break
    graph[u].append(v)
    graph[v].append(u)
scores = [n + 1] * (n + 1)
ms = n + 1
msl = []
for i in range(1, n + 1):
    q = deque([i])
    distance = [-1] * (n + 1)
    distance[i] = 0
    md = 0
    while q:
        v = q.popleft()
        md = max(md, distance[v])
        for u in graph[v]:
            if distance[u] == -1:
                distance[u] = distance[v] + 1
                q.append(u)
    scores[i] = md
    if scores[i] < ms:
        ms = scores[i]
        msl.clear()
        msl.append(i)
    elif scores[i] == ms:
        msl.append(i)
print(ms, len(msl))
print(*msl)
