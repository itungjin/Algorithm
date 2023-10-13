import sys

sys.setrecursionlimit(200000)

input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
visited = [False] * (N + 1)
subtree = [0] * (N + 1)


def solution(root):
    visited[root] = True
    cnt = 1
    for v in graph[root]:
        if visited[v]:
            continue
        cnt += solution(v)
    subtree[root] = cnt
    return cnt

solution(R)
for _ in range(Q):
    print(subtree[int(input().rstrip())])
