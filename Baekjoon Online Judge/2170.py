import sys

INF = -int(1e9)
input = sys.stdin.readline

N = int(input().rstrip())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()

answer = 0
last_y = INF
for x, y in points:
    if y <= last_y:
        continue
    if x < last_y:
        answer += y - last_y
        last_y = y
    else:
        answer += y - x
        last_y = y
print(answer)
