import sys

INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A, B, T = map(int, input().split())
    cost[A - 1][B - 1] = T
for i in range(N):
    cost[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            tmp = cost[i][k] + cost[k][j]
            if tmp < cost[i][j]:
                cost[i][j] = tmp
K = int(input().rstrip())
C = list(map(int, input().split()))
min_time = INF
X = []
for i in range(N):
    tmp = 0
    for j in range(K):
        tmp2 = cost[i][C[j] - 1] + cost[C[j] - 1][i]
        if tmp2 > tmp:
            tmp = tmp2
    if min_time > tmp:
        min_time = tmp
        X.clear()
        X.append(i + 1)
    elif min_time == tmp:
        X.append(i + 1)
print(*X)
