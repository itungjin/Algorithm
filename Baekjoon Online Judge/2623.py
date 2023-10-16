import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * 1001
graph = [[] for _ in range(1001)]
answer = []
for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, len(order) - 1):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1


def topology_sort():
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        answer.append(v)
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)


topology_sort()
if len(answer) != N:
    print(0)
else:
    for i in range(len(answer)):
        print(answer[i])
