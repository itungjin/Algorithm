import sys

input = sys.stdin.readline

N = int(input().rstrip())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: (x[1], x[0]))
for point in points:
    print(*point)
