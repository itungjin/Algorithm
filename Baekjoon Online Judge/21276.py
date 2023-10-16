import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
names = input().split()
names.sort()
name_to_num = {}
i = 0
for name in names:
    name_to_num[name] = i
    i += 1
M = int(input().rstrip())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y = input().split()
    graph[name_to_num[Y]].append(name_to_num[X])
    indegree[name_to_num[X]] += 1

children = [[] for _ in range(N + 1)]
ancestors = []
for i in range(N):
    if indegree[i] == 0:
        ancestors.append(i)
print(len(ancestors))
for ancestor in ancestors:
    print(names[ancestor], end=' ')
    q = deque([ancestor])
    while q:
        v = q.popleft()
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)
                children[v].append(u)
print()
for i in range(N):
    print(names[i], len(children[i]), end=' ')
    children[i].sort()
    for j in range(len(children[i])):
        print(names[children[i][j]], end=' ')
    print()