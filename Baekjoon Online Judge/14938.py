import sys

INF = int(1e9)

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
cost = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    cost[a - 1][b - 1] = l
    cost[b - 1][a - 1] = l
for k in range(n):
    for i in range(n):
        for j in range(n):
            tmp = cost[i][k] + cost[k][j]
            if tmp < cost[i][j]:
                cost[i][j] = tmp
ans = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if cost[i][j] <= m:
            tmp += items[j]
    if tmp > ans:
        ans = tmp
print(ans)
