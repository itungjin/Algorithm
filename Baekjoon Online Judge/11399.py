import sys

input = sys.stdin.readline

N = int(input().rstrip())
P = list(map(int, input().split()))
P.sort()
now = 0
answer = 0
for time in P:
    now += time
    answer += now
print(answer)
