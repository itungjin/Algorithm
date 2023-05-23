# 그리디
# N은 동전의 개수

n = int(input())
coins = list(map(int, input().split()))
answer = 1

coins.sort()
for coin in coins:
    if answer - coin >= 0:
        answer = answer + coin
    else:
        break

print(answer)
