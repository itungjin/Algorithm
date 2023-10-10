import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
distance = [-1] * (N + 1)
distance[1] = 0
q = deque([1])
longest_list = []
longest = 0
while q:
    v = q.popleft()
    if distance[v] > longest:
        longest_list.clear()
        longest_list.append(v)
        longest = distance[v]
    elif distance[v] == longest:
        longest_list.append(v)
    for u in graph[v]:
        if distance[u] == -1:
            distance[u] = distance[v] + 1
            q.append(u)
longest_list.sort()
print(longest_list[0], longest, len(longest_list))
