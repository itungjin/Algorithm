# 구현

import sys

input = sys.stdin.readline

A, B = map(int, input().split())

while not (A == 0 and B == 0):
    print(A + B)

    A, B = map(int, input().split())
