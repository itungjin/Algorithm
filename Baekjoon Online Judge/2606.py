import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
answer = 0
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])
while q:
    u = q.popleft()
    for v in graph[u]:
        if visited[v]:
            continue
        visited[v] = True
        answer += 1
        q.append(v)

print(answer)
