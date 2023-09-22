import sys

input = sys.stdin.readline

T = int(input().rstrip())
N = 1000001
dp = [0] * N
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, N):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(T):
    n = int(input().rstrip())
    print(dp[n])
