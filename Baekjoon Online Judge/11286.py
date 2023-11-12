import sys
import heapq

input = sys.stdin.readline

min_heap = []
max_heap = []

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())

    if x == 0:
        if max_heap and min_heap:
            if min_heap[0] >= max_heap[0]:
                print(-heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap))
        elif max_heap:
            print(-heapq.heappop(max_heap))
        elif min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)

    else:
        if x > 0:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
