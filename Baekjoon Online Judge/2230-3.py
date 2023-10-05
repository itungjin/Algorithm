import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input().rstrip()) for _ in range(N)]
A.sort()
answer = 2000000001
start = 0
for i in range(N):
    if A[i] - A[0] >= M:
        start = i
        answer = A[i] - A[0]
        break
for left in range(1, N):
    for right in range(start, N):
        result = A[right] - A[left]
        if result >= M:
            start = right
            if result < answer:
                answer = result
            break
print(answer)