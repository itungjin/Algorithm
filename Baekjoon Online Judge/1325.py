import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
count_max = 0
answer = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[i] = True
    q = deque([i])
    count = 0
    while q:
        v = q.popleft()
        count += 1
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    if count > count_max:
        count_max = count
        answer.clear()
        answer.append(i)
    elif count == count_max:
        answer.append(i)
print(*answer)
