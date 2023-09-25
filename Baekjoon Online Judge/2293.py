import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
dp = [0] * (k + 1)
for coin in coins:
    if coin <= k:
        dp[coin] += 1
    for i in range(k):
        if i + coin < k + 1:
            if dp[i] != 0:
                dp[i + coin] += dp[i]
        else:
            break
print(dp[k])
