import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
d = [1] * N
answer = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)
    answer = max(answer, d[i])
print(answer)
