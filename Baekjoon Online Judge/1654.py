import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lans = [int(input().rstrip()) for _ in range(K)]

start = 0
end = max(lans)

while start < end:
    mid = (start + end + 1) // 2
    count = 0
    for lan in lans:
        count += lan // mid
    if count >= N:
        start = mid
    else:
        end = mid - 1
print(start)
