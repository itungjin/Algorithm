import sys

input = sys.stdin.readline

# 수가 처음 입력된 인덱스, 수가 등장한 횟수가 중요

N, C = map(int, input().split())
# nums의 원소는 1보다 크고 C보다 같거나 작다.
nums = list(map(int, input().split()))

when_entered = {}
for i in range(N):
    if nums[i] not in when_entered:
        when_entered[nums[i]] = (i, nums[i])

count = [[] for _ in range(1001)]
nums.sort()

c = 1
for i in range(1, N):
    if nums[i] != nums[i - 1]:
        count[c].append(nums[i - 1])
        c = 0
    c += 1
count[c].append(nums[-1])

for i in range(len(count) - 1, 0, -1):
    if len(count[i]) > 1:
        tmp = []
        for j in range(len(count[i])):
            tmp.append(when_entered[count[i][j]])
        tmp.sort()
        for j in range(len(tmp)):
            for _ in range(i):
                print(tmp[j][1], end=' ')
    elif len(count[i]) == 1:
        for _ in range(i):
            print(count[i][0], end=' ')
