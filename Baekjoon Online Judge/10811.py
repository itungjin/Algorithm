# 구현

N, M = map(int, input().split())

baskets = [i for i in range(0, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = baskets[i:j+1]
    temp.reverse()
    baskets[i:j+1] = temp

for i in range(1, N + 1):
    print(baskets[i], end=' ')
