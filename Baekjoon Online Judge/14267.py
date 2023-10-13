import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(map(int, input().split()))
graph = [set() for _ in range(n + 1)]
praise = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    graph[parent[i - 1]].add(i)
    praise[i] += w
answer = [0] * (n + 1)
for i in range(1, n + 1):
    if answer[i] != 0:
        continue
    answer[i] = answer[parent[i - 1]]
    q = deque([i])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            q.append(nxt)
            answer[nxt] = answer[cur] + praise[nxt]
print(*answer[1:])
