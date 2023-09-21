import sys

input = sys.stdin.readline

N = int(input().rstrip())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())
d = [0] * (N + 1)
available = dict()
now = 0
for i in range(N):
    if i in available and available[i] > now:
        now = available[i]
    if i + T[i] in available:
        available[i + T[i]] = max(available[i + T[i]], now + P[i])
    else:
        available[i + T[i]] = now + P[i]
if N in available and available[N] > now:
    print(available[N])
else:
    print(now)
