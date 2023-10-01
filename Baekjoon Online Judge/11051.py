N, K = map(int, input().split())
dp = [[1] * i for i in range(1, 1002)]
for i in range(1, N+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
print(dp[N][K])
