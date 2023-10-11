import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())
hypercube = [[] for _ in range(M)]
connected = [[] for _ in range(N + 1)]
distance = [-1 for _ in range(N + 1)]
distance[1] = 1
checked = [False] * M
for i in range(M):
    hypercube[i] = list(map(int, input().split()))
    for station in hypercube[i]:
        connected[station].append(i)
q = deque([1])
while q:
    v = q.popleft()
    for h in connected[v]:
        if not checked[h]:
            checked[h] = True
            for u in hypercube[h]:
                if distance[u] == -1:
                    distance[u] = distance[v] + 1
                    q.append(u)
print(distance[N])
