import sys

input = sys.stdin.readline
k = 1
while True:
    N = int(input().rstrip())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0 for _ in range(3)] for _ in range(N)]
    cost[0][1] = graph[0][1]
    cost[0][2] = graph[0][1] + graph[0][2]
    cost[1][0] = cost[0][1] + graph[1][0]
    cost[1][1] = min(cost[1][0], cost[0][1], cost[0][2]) + graph[1][1]
    cost[1][2] = min(cost[1][1], cost[0][1], cost[0][2]) + graph[1][2]
    for i in range(2, N):
        cost[i][0] = min(cost[i - 1][0], cost[i - 1][1]) + graph[i][0]
        cost[i][1] = min(cost[i - 1][0], cost[i - 1][1], cost[i - 1][2], cost[i][0]) + graph[i][1]
        cost[i][2] = min(cost[i - 1][1], cost[i - 1][2], cost[i][1]) + graph[i][2]
    print(k, ". ", cost[N - 1][1], sep="")
    k += 1
