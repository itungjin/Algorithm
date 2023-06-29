# 구현

import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    for char in S:
        print(char * R, end='')
    print()
