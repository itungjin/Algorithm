import sys
import heapq

input = sys.stdin.readline

hp = list()
hm = list()
N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if hp and hm:
            if hp[0] == hm[0]:
                print(-heapq.heappop(hm))
            elif hp[0] > hm[0]:
                print(-heapq.heappop(hm))
            else:
                print(heapq.heappop(hp))
        elif hp:
            print(heapq.heappop(hp))
        elif hm:
            print(-heapq.heappop(hm))
        else:
            print(0)
    elif x > 0:
        heapq.heappush(hp, x)
    else:
        heapq.heappush(hm, -x)
