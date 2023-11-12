import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
heap = []
for _ in range(N):
    x = int(input().rstrip())

    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
