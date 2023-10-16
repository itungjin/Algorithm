import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * 32001
graph = [[] for _ in range(32001)]
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)


def topology_sort():
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)


topology_sort()
