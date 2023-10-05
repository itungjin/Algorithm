import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input().rstrip()) for _ in range(N)]
A.sort()
answer = 2000000001
left = N - 2
right = N - 1
while left >= 0:
    result = A[right] - A[left]
    if result < M:
        left -= 1
    elif result == M:
        answer = M
        break
    else:
        answer = min(result, answer)
        if A[right - 1] - A[left]:
            right -= 1
        else:
            left -= 1
print(answer)
