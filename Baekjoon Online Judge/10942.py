import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if numbers[i] != numbers[i + 1]:
        continue
    dp[i][i + 1] = 1

for r in range(2, N):
    for i in range(N - r):
        if numbers[i] != numbers[i + r]:
            continue
        if not dp[i + 1][i + r - 1]:
            continue
        dp[i][i + r] = 1
M = int(input().rstrip())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
