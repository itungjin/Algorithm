import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
people = set()
temp = list(map(int, input().split()))
if temp[0] != 0:
    people = set(temp[1:])
participants = [[] for _ in range(M + 1)]
graph = [set() for _ in range(N + 1)]
for i in range(1, M + 1):
    participants[i] = list(map(int, input().split()))[1:]
    n = len(participants[i])
    for v in range(n):
        for u in range(v + 1, n):
            graph[participants[i][v]].add(participants[i][u])
            graph[participants[i][u]].add(participants[i][v])

visited = [False] * (N + 1)
for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = True
    t_or_f = False
    q = deque([i])
    group = [i]
    while q:
        v = q.popleft()
        if v in people:
            t_or_f = True
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
                group.append(u)
    if t_or_f:
        people.update(group)
answer = 0
for i in range(1, M + 1):
    if all(participant not in people for participant in participants[i]):
        answer += 1
print(answer)
