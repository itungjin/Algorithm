# 구현

import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            if r1 == 0:
                print(1)
            else:
                print(-1)
        else:
            print(0)
    else:
        dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        if dist > r1 + r2:
            print(0)
        elif dist == r1 + r2:
            print(1)
        else:
            if abs(r1 - r2) == dist:
                print(1)
            elif abs(r1 - r2) > dist:
                print(0)
            else:
                print(2)
