# 그리디

import sys
input = sys.stdin.readline

coins = (25, 10, 5, 1)
for _ in range(int(input().rstrip())):
    C = int(input().rstrip())

    for coin in coins:
        print(C // coin, end=' ')
        C = C % coin
    print()
