import sys

input = sys.stdin.readline

N = int(input().rstrip())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())
d = [0] * (N + 1)

for i in range(N):
    for j in range(i + T[i], N + 1):
        d[j] = max(d[j], d[i] + P[i])
print(d[N])
