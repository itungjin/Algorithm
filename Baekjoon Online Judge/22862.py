import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

right = -1
count = 0
answer = 0

for left in range(N):
    while count < K and right < N - 1:
        right += 1
        if S[right] % 2 == 1:
            count += 1
    while right < N - 1:
        if S[right + 1] % 2 == 0:
            right += 1
        else:
            break
    answer = max(answer, right - left + 1 - count)
    if S[left] % 2 == 1:
        count -= 1
print(answer)
