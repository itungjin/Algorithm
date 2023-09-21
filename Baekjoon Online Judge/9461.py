import sys

input = sys.stdin.readline

P = [1] * 101
P[1], P[2], P[3], P[4] = 1, 1, 1, 2
for i in range(5, 101):
    P[i] = P[i - 2] + P[i - 3]
T = int(input().rstrip())
for _ in range(T):
    print(P[int(input().rstrip())])
