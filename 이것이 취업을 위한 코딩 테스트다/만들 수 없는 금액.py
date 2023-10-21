import sys

input = sys.stdin.readline

N = int(input().rstrip())
coins = list(map(int, input().split()))
coins.sort()
# ans - 1까지의 금액은 만들 수 있다.
ans = 1
for coin in coins:
    if coin > ans:
        break
    # ans - 1 + coin까지의 금액은 만들 수 있다.
    ans += coin
print(ans)
