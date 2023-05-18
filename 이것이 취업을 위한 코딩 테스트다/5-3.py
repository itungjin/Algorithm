# BFS
from collections import deque


def bfs(graph, r, c):
    if graph[r][c] == 1:
        return False
    graph[r][c] = 1
    queue = deque([[r, c]])
    while queue:
        r, c = queue.popleft()
        if 0 <= r - 1 < n and 0 <= c < m:
            if graph[r - 1][c] == 0:
                graph[r - 1][c] = 1
                queue.append([r - 1, c])
        if 0 <= r + 1 < n and 0 <= c < m:
            if graph[r + 1][c] == 0:
                graph[r + 1][c] = 1
                queue.append([r + 1, c])
        if 0 <= r < n and 0 <= c - 1 < m:
            if graph[r][c - 1] == 0:
                graph[r][c - 1] = 1
                queue.append([r, c - 1])
        if 0 <= r < n and 0 <= c + 1 < m:
            if graph[r][c + 1] == 0:
                graph[r][c + 1] = 1
                queue.append([r, c + 1])
    return True


n, m = map(int, input().split())  # 1 <= n, m <= 1000
case = [list(map(int, input())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if bfs(case, i, j):
            answer += 1

print(answer)
