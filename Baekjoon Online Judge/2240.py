import sys

input = sys.stdin.readline

T, W = map(int, input().split())
p = [int(input().rstrip()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T)]
if p[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1
for i in range(1, T):
    if p[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    for j in range(1, W + 1):
        if i + 1 < j:
            break
        if j % 2 == 0:
            if p[i] == 1:
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        else:
            if p[i] == 2:
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[T - 1]))
