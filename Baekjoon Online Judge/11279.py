import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
array = []
for _ in range(N):
    x = int(input().rstrip())

    if x > 0:
        heapq.heappush(array, -x)
    else:
        if array:
            print(-heapq.heappop(array))
        else:
            print(0)
