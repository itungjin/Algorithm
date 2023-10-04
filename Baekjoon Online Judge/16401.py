import sys

input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))
start = 0
end = 1000000000
while start < end:
    mid = (start + end + 1) // 2
    count = 0
    for l in L:
        count += l // mid
    if count >= M:
        start = mid
    else:
        end = mid - 1
print(start)
