import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
dp = []
answer = A[0]
for i in range(N):
    temp = A[i]
    for a, b in dp:
        if a < A[i]:
            temp = max(temp, b + A[i])
    answer = max(answer, temp)
    dp.append((A[i], temp))
print(answer)
