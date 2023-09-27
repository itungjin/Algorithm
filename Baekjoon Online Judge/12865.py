import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(K + 1)]
dp[0] = 0
for w, v in items:
    for i in range(K - w, -1, -1):
        if dp[i] != -1:
            dp[i + w] = max(dp[i + w], dp[i] + v)
print(max(dp))
