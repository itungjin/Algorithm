import sys

INF = int(1e9)

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
cost = [[1e9] * n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)
for v in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][v] + cost[v][j])
for i in range(n):
    for j in range(n):
        if cost[i][j] == 1e9:
            cost[i][j] = 0
for i in range(n):
    for j in range(n):
        print(cost[i][j], end=' ')
    print()
