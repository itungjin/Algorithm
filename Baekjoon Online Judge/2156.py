import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

if n <= 2:
    print(sum(arr))
    exit(0)
dp = [[0] * 3 for _ in range(n)]
dp[0][1] = arr[0]
dp[1][0] = arr[0]
dp[1][1] = arr[1]
dp[1][2] = arr[0] + arr[1]
for i in range(2, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + arr[i]
    dp[i][2] = dp[i - 1][1] + arr[i]
print(max(dp[n - 1]))
