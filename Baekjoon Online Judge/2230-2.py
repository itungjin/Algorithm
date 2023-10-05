import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input().rstrip()) for _ in range(N)]
A.sort()
answer = 2000000001
for left in range(N):
    right = bisect_left(A, A[left] + M)
    if right < N:
        answer = min(answer, A[right] - A[left])
print(answer)
