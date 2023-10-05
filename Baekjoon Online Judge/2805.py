import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = 2000000000
while start < end:
    mid = (start + end + 1) // 2
    count = 0
    for tree in trees:
        if tree > mid:
            count += tree - mid
    if count >= M:
        start = mid
    else:
        end = mid - 1
print(start)