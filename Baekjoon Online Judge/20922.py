import sys

input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

nums = [0] * 100001
answer = 0
right = -1
for left in range(N):
    while right < N - 1 and nums[a[right + 1]] < K:
        right += 1
        nums[a[right]] += 1
    answer = max(answer, right - left + 1)
    nums[a[left]] -= 1
print(answer)
