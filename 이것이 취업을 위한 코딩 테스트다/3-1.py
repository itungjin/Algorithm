# 그리디
# 큰 단위의 동전을 최대한 많이 사용

n = 1260
coins = [500, 100, 50, 10]
answer = 0

for coin in coins:
    answer += n // coin
    n %= coin

print(answer)
