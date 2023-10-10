import sys

input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
distance = [-1] * (n + 1)
distance[1] = 0
q = deque([1])
answer = 0
while q:
    v = q.popleft()
    if distance[v] <= 1:
        for u in graph[v]:
            if distance[u] == -1:
                distance[u] = distance[v] + 1
                q.append(u)
                answer += 1
print(answer)
