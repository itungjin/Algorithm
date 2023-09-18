import sys

input = sys.stdin.readline
N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
nums.sort()
for num in nums:
    print(num)
