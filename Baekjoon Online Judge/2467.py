import sys
from bisect import bisect_left

input = sys.stdin.readline
N = int(input().rstrip())
data = list(map(int, input().split()))
min_abs = 2000000001
ans1, ans2 = 0, 0

for i in range(N):
    index = bisect_left(data, -data[i])
    if index + 1 <= N - 1 and index + 1 != i and abs(data[i] + data[index + 1]) < min_abs:
        min_abs = abs(data[i] + data[index + 1])
        ans1, ans2 = data[i], data[index + 1]
    if index <= N - 1 and index != i and abs(data[i] + data[index]) < min_abs:
        min_abs = abs(data[i] + data[index])
        ans1, ans2 = data[i], data[index]
    if index != 0 and index - 1 != i and abs(data[i] + data[index - 1]) < min_abs:
        min_abs = abs(data[i] + data[index - 1])
        ans1, ans2 = data[i], data[index - 1]
if ans1 < ans2:
    print(ans1, ans2)
else:
    print(ans2, ans1)
