import sys

input = sys.stdin.readline
N = int(input().rstrip())
count = [0] * 10001
for _ in range(N):
    count[int(input().rstrip())] += 1
for i in range(1, 10001):
    for j in range(count[i]):
        print(i)
