# 구현

N, k = map(int, input().split())

order = 1
for i in range(1, N + 1):
    if N % i == 0:
        if order == k:
            print(i)
            order += 1
            break
        order += 1

if order <= k:
    print(0)
