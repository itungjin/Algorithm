import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input().rstrip()) for _ in range(N)]
result = 0
i = N - 1
while K != 0:
    if A[i] > K:
        i -= 1
        continue
    result += K // A[i]
    K %= A[i]
    i -= 1
print(result)
