# 스택

import sys
from collections import deque
input = sys.stdin.readline

recent = deque()
total = 0

K = int(input().rstrip())
for _ in range(K):
    integer = int(input().rstrip())
    if integer == 0:
        total -= recent.pop()
    else:
        recent.append(integer)
        total += integer

print(total)
