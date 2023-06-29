# 구현

import sys

input = sys.stdin.readline

for _ in range(100):
    try:
        print(input().rstrip())
    except:
        break
