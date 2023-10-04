import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
nums.sort()
max_value = nums[0]
max_count = 1
count = 1
for i in range(1, N):
    if nums[i] != nums[i-1]:
        if count > max_count:
            max_value = nums[i-1]
            max_count = count
        count = 0
    count += 1
if count > max_count:
    max_value = nums[-1]
print(max_value)