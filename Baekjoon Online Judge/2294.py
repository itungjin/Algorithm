import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(set([int(input().rstrip()) for _ in range(n)]))
dp = [0] * (k + 1)
for coin in coins:
    if coin > k:
        continue
    dp[coin] = 1
    for i in range(coin + 1, k + 1):
        if dp[i - coin] == 0:
            continue
        if dp[i] == 0:
            dp[i] = dp[i - coin] + 1
        else:
            dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k]:
    print(dp[k])
else:
    print(-1)
