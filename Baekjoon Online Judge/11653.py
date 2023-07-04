# 구현

N = int(input())

for i in range(2, N + 1):
    while N % i == 0:
        N //= i
        print(i)
    if N == 1:
        break
