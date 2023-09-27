import sys

input = sys.stdin.readline
N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
nums.sort(reverse=True)
answer = 0
i = 0
while i < N:
    if nums[i] > 0:
        if i + 1 < N and nums[i + 1] > 1:
            answer += nums[i] * nums[i + 1]
            i += 2
        else:
            answer += nums[i]
            i += 1
    else:
        break
j = N - 1
while j >= i:
    if nums[j] < 0:
        if j - 1 >= 0 and nums[j - 1] <= 0:
            answer += nums[j] * nums[j - 1]
            j -= 2
        else:
            answer += nums[j]
            j -= 1
    else:
        break
print(answer)
