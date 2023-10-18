import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
cost = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
nxt = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < cost[a][b]:
        cost[a][b] = c
        nxt[a][b] = b
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tmp = cost[i][k] + cost[k][j]
            if tmp < cost[i][j]:
                cost[i][j] = tmp
                nxt[i][j] = nxt[i][k]
for i in range(1, n + 1):
    cost[i][i] = INF
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == INF:
            print(0)
        else:
            now = i
            tmp = [i]
            while now != j:
                now = nxt[now][j]
                tmp.append(now)
            print(len(tmp), *tmp)
