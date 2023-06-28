# 구현

import sys

input = sys.stdin.readline

N = int(input().rstrip())
integers = list(map(int, input().split()))

print(min(integers), max(integers))
