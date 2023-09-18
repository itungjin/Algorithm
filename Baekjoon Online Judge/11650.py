import sys

input = sys.stdin.readline

N = int(input().rstrip())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()
for point in points:
    print(*point)
