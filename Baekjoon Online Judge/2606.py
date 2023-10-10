import sys
from collections import deque

input = sys.stdin.readline

graph = [[] for _ in range(101)]
nv = int(input().rstrip())
ne = int(input().rstrip())
for _ in range(ne):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * 101
visited[1] = True
answer = 0
q = deque([1])
while q:
    v = q.popleft()
    for u in graph[v]:
        if not visited[u]:
            q.append(u)
            visited[u] = True
            answer += 1
print(answer)
