import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
answer = 0
A.sort()
for i in range(N):
    left = i + 1
    right = N - 1
    while left < right:
        sum = A[i] + A[left] + A[right]
        if sum == 0:
            if A[left] != A[right]:
                nl = bisect_right(A, A[left])
                nr = bisect_left(A, A[right])
                answer += (nl - left) * (right + 1 - nr)
                left = nl
                right = nr - 1
            else:
                answer += (right - left + 1) * (right - left) // 2
                break
        elif sum < 0:
            left += 1
        else:
            right -= 1
print(answer)
