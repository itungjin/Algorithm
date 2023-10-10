import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
min_kb = N * (N - 1) // 2
min_kb_idx = -1
for i in range(1, N + 1):
    kb = [-1] * (N + 1)
    kb[0] = 0
    kb[i] = 0
    q = deque([i])
    while q:
        v = q.popleft()
        for u in graph[v]:
            if kb[u] == -1:
                kb[u] = kb[v] + 1
                q.append(u)
    skb = sum(kb)
    if min_kb > skb:
        min_kb = skb
        min_kb_idx = i
print(min_kb_idx)
