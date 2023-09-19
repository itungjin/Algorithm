import sys

input = sys.stdin.readline

n = list(input().split())
nums = [0] * int(n[0])
i = 0
if len(n) > 1:
    while i < len(n) - 1:
        nums[i] = int(n[i + 1][::-1])
        i += 1
n = int(n[0])
while True:
    if i == n:
        break
    arr = input().split()
    for j in range(len(arr)):
        nums[i] = int(arr[j][::-1])
        i += 1
nums.sort()
for num in nums:
    print(num)
