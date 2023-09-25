import sys

input = sys.stdin.readline

N = int(input().rstrip())
P = list(map(int, input().split()))
dp = [0] * N
dp[0] = P[0]
for i in range(1, N):
    dp[i] = P[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + P[i - j - 1])
print(dp[N - 1])
