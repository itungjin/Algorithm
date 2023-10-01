import sys
import math
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    max_val = math.lcm(M, N)
    if x == M and N == y:
        print(max_val)
        continue
    if x == M:
        x = 0
    if y == N:
        y = 0
    a = x
    while a < max_val:
        if a % N == y:
            break
        a += M
    if a % N == y:
        print(a)
    else:
        print(-1)