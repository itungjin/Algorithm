import sys

input = sys.stdin.readline

N = int(input().rstrip())
coins = list(map(int, input().split()))
coins.sort()
ans = 1
for coin in coins:
    if coin > ans:
        break
    ans += coin
print(ans)