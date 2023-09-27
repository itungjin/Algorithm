import sys

input = sys.stdin.readline

N = int(input().rstrip())
dat = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dat.sort(key=lambda x: (x[1], x[0]))
now = 0
for start, end in dat:
    if start >= now:
        now = end
        answer += 1
print(answer)
