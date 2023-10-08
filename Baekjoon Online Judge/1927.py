import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
heap = list()
for _ in range(N):
    x = int(input().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
