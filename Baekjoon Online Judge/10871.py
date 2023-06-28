# 완전 탐색

import sys

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

for number in A:
    if number < X:
        print(number, end=' ')
